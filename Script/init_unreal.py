from utils.unreal_extensions import ImportAssetStruct, ImportedAssetData
import unreal
unreal.log_warning("Init")

@unreal.uclass()
class PythonExposedClass(unreal.BlueprintFunctionLibrary):
    def __init__(self):
        super().__init__()

    @unreal.ufunction(static=True, params=[ImportAssetStruct], ret=unreal.Array(ImportedAssetData))
    def preview_assets(importAssetDto: ImportAssetStruct):
        pass

    @unreal.ufunction(static=True, params=[unreal.Array(ImportedAssetData)])
    def import_assets(assetsToImport: unreal.Array(ImportedAssetData)):
        pass