from direct.showbase.ShowBase import ShowBase
from panda3d.core import Filename, AmbientLight, DirectionalLight, Vec4

class ToonGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        # Load a sample environment (Cog HQ Interior)
        self.environment = self.loader.loadModel("assets/phase_6/models/neighborhoods/donalds_dock.bam")
        self.environment.reparentTo(self.render)
        
        # Set position and scale
        self.environment.setPos(0, 0, 0)
        self.environment.setScale(1)
        
        # Add ambient lighting
        ambient_light = AmbientLight("ambient")
        ambient_light.setColor(Vec4(0.5, 0.5, 0.5, 1))
        ambient_node = self.render.attachNewNode(ambient_light)
        self.render.setLight(ambient_node)
        
        # Add directional lighting
        directional_light = DirectionalLight("directional")
        directional_light.setColor(Vec4(0.8, 0.8, 0.8, 1))
        directional_node = self.render.attachNewNode(directional_light)
        directional_node.setHpr(-45, -45, 0)
        self.render.setLight(directional_node)
        
        # Set up basic camera controls
        self.disableMouse()
        self.taskMgr.add(self.moveCameraTask, "MoveCameraTask")

    def moveCameraTask(self, task):
        # Basic WASD-style camera movement (placeholder, can improve later)
        speed = 5 * globalClock.getDt()
        if self.mouseWatcherNode.isButtonDown("w"): 
            self.camera.setY(self.camera, speed)
        if self.mouseWatcherNode.isButtonDown("s"): 
            self.camera.setY(self.camera, -speed)
        if self.mouseWatcherNode.isButtonDown("a"): 
            self.camera.setX(self.camera, -speed)
        if self.mouseWatcherNode.isButtonDown("d"): 
            self.camera.setX(self.camera, speed)
        return task.cont

# Run the game
app = ToonGame()
app.run()