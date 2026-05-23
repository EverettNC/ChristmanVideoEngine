import os
import subprocess
import sys

class ChristmanOrchestrator:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.installer_path = os.path.join(self.base_dir, "ChristmanMediaInstaller")
        self.sdk_path = os.path.join(self.base_dir, "Christman-Sound")
        
        # Add Sound SDK to system path to allow 'from CHRISTMAN_EAR_CANAL import ...'
        if self.sdk_path not in sys.path:
            sys.path.append(self.sdk_path)

    def verify_readiness(self, being_path):
        """Invoke Media Installer Truth Report."""
        print(f"[Orchestrator] Running Truth Report on: {being_path}")
        # Call the CLI
        result = subprocess.run(
            [sys.executable, "-m", "christman_media_installer.cli", "verify", "--target", being_path],
            cwd=self.installer_path, capture_output=True, text=True
        )
        print(result.stdout)
        return "READY" in result.stdout

    def speak(self, text, emotion="warm"):
        """Invoke Christman-Sound SPEAK engine."""
        try:
            from CHRISTMAN_EAR_CANAL import SPEAK
            print(f"[Orchestrator] Speaking: {text}")
            SPEAK.speak(text, emotion=emotion)
        except ImportError as e:
            print(f"CRITICAL: Christman-Sound SDK not reachable. Error: {e}")
