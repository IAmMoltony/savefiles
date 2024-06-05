from backupper_minecraft import MinecraftBackupper
from backupper_touhou import Touhou06Backupper, Touhou07Backupper, Touhou08Backupper, Touhou10Backupper, Touhou18Backupper
from backupper_babaisyou import BabaIsYouBackupper
from backupper_supertux import SuperTuxBackupper
from backupper_forager import ForagerBackupper

BACKUPPERS = {
    "Minecraft": MinecraftBackupper,
    "Touhou06": Touhou06Backupper,
    "Touhou07": Touhou07Backupper,
    "Touhou08": Touhou08Backupper,
    "Touhou10": Touhou10Backupper,
    "Touhou18": Touhou18Backupper,
    "BabaIsYou": BabaIsYouBackupper,
    "SuperTux": SuperTuxBackupper,
    "Forager": ForagerBackupper
}
