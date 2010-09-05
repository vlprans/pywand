from ctypes import *

_libraries = {}
from ctypes.util import find_library
_libraries['MagickWand'] = CDLL(find_library('MagickWand'))
_lib = _libraries['MagickWand']
STRING = c_char_p


LocaleEvent = 512
TriangleFilter = 3
DifferenceCompositeOp = 26
PointFilter = 1
BlobTransmitType = 2
PixelsPerInchResolution = 1
SubimagePath = 7
OpenMorphology = 8
DisassociatedQuantumAlpha = 2
EdgeMorphology = 15
UndefinedFilter = 0
BohmanFilter = 20
ConfigureWarning = 395
PlusCompositeOp = 42
PointMethod = 1
RotatePreview = 1
MagickResourceOptions = 58
CMYKColorspace = 12
MagickPath = 1
UniformNoise = 1
GaussianKernel = 2
ImageError = 465
VividLightCompositeOp = 59
ArcsinFunction = 3
IndexChannel = 32
UndefinedRule = 0
TransparentVirtualPixelMethod = 8
BesselFilter = 14
MagickIntentOptions = 31
FileOpenWarning = 330
CrossKernel = 19
ColorSeparationMatteType = 9
SwirlPreview = 24
RGBQuantum = 18
PolarDistortion = 10
StreamFatalError = 740
ChebyshevKernel = 30
RandomVirtualPixelMethod = 6
CorrelateMorphology = 2
AndEvaluateOperator = 2
ExecutePolicyRights = 4
RiemersmaDitherMethod = 2
LeftAlign = 1
CopyCompositeOp = 13
AbsoluteIntent = 3
UndefinedTimerState = 0
GaussianNoiseEvaluateOperator = 18
TransformEvent = 8192
BlackmanFilter = 7
UndefinedDistortion = 0
BlobWarning = 335
HardLightCompositeOp = 30
YUVColorspace = 11
NoThreadSupport = 0
RaisePreview = 22
GaussianFilter = 8
MagickMimeOptions = 45
UserSpace = 1
ThinningMorphology = 19
CMYColorspace = 22
RhoValue = 4
TypeError = 405
EdgeDetectPreview = 18
SoftLightCompositeOp = 46
LZWCompression = 11
UndefinedDitherMethod = 0
MagickTypeOptions = 64
MagickStyleOptions = 62
CompassKernel = 12
LaplacianNoise = 5
CMYKQuantum = 5
MonitorError = 485
MathematicsCompositeOp = 63
GrayChannels = 128
ImageInfoRegistryType = 2
UndefinedPolicyRights = 0
NormalStyle = 1
StringRegistryType = 3
UndefinedResource = 0
MagickUndefinedOptions = -1
CbYCrYQuantum = 22
ModuleFatalError = 755
UndefinedCompositeOp = 0
DirectClass = 1
UndefinedPrimitive = 0
AnyStyle = 4
BlackVirtualPixelMethod = 10
PaletteMatteType = 5
BoxFilter = 2
MagickDecorateOptions = 15
UndefinedQuantum = 0
MaxEvaluateOperator = 5
TraceEvent = 1
IdentifyValidate = 32
DespecklePreview = 12
CopyOpacityCompositeOp = 17
DullPreview = 9
RightBottomOrientation = 7
UnderlineDecoration = 2
DilateIntensityMorphology = 6
CatromFilter = 11
PerspectiveDistortion = 4
FilterWarning = 352
LightenCompositeOp = 33
UndefinedEvaluateOperator = 0
PreviousDispose = 3
WavePreview = 26
BicubicInterpolatePixel = 2
MagickNoiseOptions = 49
ExplicitFormatType = 2
ExtraExpandedStretch = 8
CorruptImageError = 425
RedQuantum = 14
SrcOutCompositeOp = 50
PizCompression = 15
BilinearColorInterpolate = 7
CyanChannel = 1
AlphaChannel = 8
CorruptImageFatalError = 725
MontageValidate = 128
OverlineDecoration = 3
UndefinedType = 0
GreenQuantum = 9
FatalErrorException = 700
RightToLeftDirection = 1
ShepardsColorInterpolate = 14
BrightnessPreview = 6
CompositeValidate = 2
ExtensionPath = 6
MapResource = 4
RandomFatalError = 775
ForgetGravity = 0
ReadMode = 0
BlendCompositeOp = 4
DelegatePolicyDomain = 2
LagrangeFilter = 19
RoundRectanglePrimitive = 4
AverageInterpolatePixel = 1
VerticalTileVirtualPixelMethod = 14
RGBOQuantum = 17
BezierPrimitive = 10
MagickDistortOptions = 19
CompareAnyLayer = 2
BackgroundAlphaChannel = 2
JPEGPreview = 29
RightShiftEvaluateOperator = 9
CoderEvent = 16
CorruptImageWarning = 325
MosaicLayer = 15
DstAtopCompositeOp = 21
IntegerPixel = 4
GRAYColorspace = 2
MagickLineCapOptions = 36
DivideEvaluateOperator = 3
RootPath = 2
ActivateAlphaChannel = 1
AddModulusEvaluateOperator = 26
OpenIntensityMorphology = 10
PercentValue = 4096
UndefinedSpread = 0
WandWarning = 370
ModulateCompositeOp = 37
BZipCompression = 2
Rec601YCbCrColorspace = 18
UndefinedDirection = 0
ModuleEvent = 1024
UndefinedQuantumFormat = 0
FloatPixel = 3
UndefinedMode = 0
CacheError = 445
XorCompositeOp = 54
SinusoidFunction = 2
CharPixel = 1
YellowChannel = 4
MagickLogEventOptions = 40
DiamondKernel = 14
PaletteType = 4
OpacityQuantum = 13
DelegateFatalError = 715
FileResource = 3
BackgroundVirtualPixelMethod = 1
CorrelateNormalizeValue = 65536
ImpulseNoise = 4
MagickCoderOptions = 6
ConvolveMorphology = 1
ConfigureFatalError = 795
WestGravity = 4
MSBEndian = 2
UndefinedPreview = 0
OpaqueAlphaChannel = 6
UnityKernel = 1
ExtraCondensedStretch = 3
WidthValue = 4
XYZColorspace = 6
ThickenMorphology = 20
FileTransmitType = 1
MeanErrorPerPixelMetric = 3
AssociatedQuantumAlpha = 1
EdgeOutMorphology = 14
DelegateWarning = 315
RegistryWarning = 390
LeftBottomOrientation = 8
ThresholdPreview = 17
OverlayCompositeOp = 41
FaxCompression = 6
PartitionInterlace = 4
ImportExportValidate = 64
AtopCompositeOp = 3
UnsignedQuantumFormat = 3
DrawError = 460
PegtopLightCompositeOp = 58
PlusKernel = 18
ArcDistortion = 9
BlobFatalError = 735
DrawFatalError = 760
BevelJoin = 3
OptimizeImageLayer = 7
LogEvaluateOperator = 14
FilterError = 452
TopRightOrientation = 2
MagickComposeOptions = 10
SignedQuantumFormat = 2
AddEvaluateOperator = 1
KaiserFilter = 16
UndefinedClass = 0
OptimizeLayer = 6
CopyBlueCompositeOp = 12
PerceptualIntent = 2
HuePreview = 4
TransparentAlphaChannel = 10
ThresholdWhiteEvaluateOperator = 17
ResourceEvent = 4096
HammingFilter = 6
ExclusionCompositeOp = 29
ChiValue = 16
SmoothMorphology = 12
MagickLogOptions = 41
RootMeanSquaredErrorMetric = 7
HitAndMissMorphology = 18
ResourceLimitError = 400
ScreenCompositeOp = 45
LosslessJPEGCompression = 10
BarycentricColorInterpolate = 1
BlurKernel = 5
RoundJoin = 2
RightAlign = 3
CMYKAQuantum = 4
XServerError = 480
LinearBurnCompositeOp = 62
YPbPrColorspace = 10
RGBChannels = 128
UndefinedStyle = 0
BasePath = 5
EdgesKernel = 22
ColorSeparationType = 8
BarrelInverseDistortion = 13
FilterFatalError = 752
MagickFalse = 0
ArctanFunction = 4
CoderPolicyDomain = 1
CenterAlign = 2
MaskVirtualPixelMethod = 9
MagickLayerOptions = 35
MagickDebugOptions = 14
CharcoalDrawingPreview = 28
LeftShiftEvaluateOperator = 4
NoEvents = 0
ResourceLimitWarning = 300
RemoveDupsLayer = 10
UndefinedMagickLayerMethod = 0
CopyMagentaCompositeOp = 16
RightTopOrientation = 6
MultiplicativeNoiseEvaluateOperator = 21
ErodeIntensityMorphology = 5
CubicFilter = 10
CoderWarning = 350
InCompositeOp = 32
HSBColorspace = 14
NoDitherMethod = 1
OHTAColorspace = 4
BackgroundDispose = 2
ImplodePreview = 25
MagickMorphologyOptions = 48
ImplicitFormatType = 1
SrcInCompositeOp = 49
ZipSCompression = 14
GrayChannel = 1
LeftToRightDirection = 2
MagickValidateOptions = 65
IndexAlphaQuantum = 10
FreiChenKernel = 9
XiNegative = 32
PolicyError = 499
PolynomialColorInterpolate = 8
AllCompliance = 2147483647
WritePolicyRights = 2
CompareValidate = 1
ResetMethod = 5
AspectValue = 8192
LineEndsKernel = 25
MagickBooleanOptions = 2
UndefinedMorphology = 0
WandFatalError = 770
UndefinedGravity = 0
RectanglePrimitive = 3
HorizontalTileVirtualPixelMethod = 13
MagickDisposeOptions = 18
OrEvaluateOperator = 8
CacheEvent = 8
SVGCompliance = 1
YValue = 2
MissingDelegateWarning = 320
FlattenLayer = 14
NoValue = 0
RGBColorspace = 1
ColorBurnCompositeOp = 8
BottomRightOrientation = 3
MagickFillRuleOptions = 23
SineEvaluateOperator = 25
CloseMorphology = 9
RadialGradient = 2
SouthEastGravity = 9
ImageWarning = 365
MinusCompositeOp = 36
NoCompression = 1
Rec601LumaColorspace = 17
UndefinedCompliance = 0
OutCompositeOp = 39
MagickPolicyDomainOptions = 52
DoublePixel = 2
StreamError = 440
ThresholdCompositeOp = 53
B44ACompression = 18
BlueChannel = 4
MagickModeOptions = 46
RandomError = 475
ImageRegistryType = 1
DrawWarning = 360
GrayscaleMatteType = 3
Group4Compression = 7
MagentaQuantum = 12
OptionFatalError = 710
FormatsOnDiskValidate = 16
ItalicStyle = 2
UndefinedVirtualPixelMethod = 0
TimeResource = 7
MinimumValue = 65536
SkeletonKernel = 29
MagickClipPathOptions = 5
SemiCondensedStretch = 5
RegistryFatalError = 790
NorthEastGravity = 3
CoalesceLayer = 1
ClearCompositeOp = 7
CirclePrimitive = 7
CheckerTileVirtualPixelMethod = 17
LSBEndian = 1
DiskKernel = 17
MagickEvaluateOptions = 22
ExtractAlphaChannel = 5
XorEvaluateOperator = 12
DrawEvent = 128
UltraCondensedStretch = 2
AreaValue = 131072
DstOutCompositeOp = 24
LabColorspace = 5
CacheWarning = 345
UndefinedTransmitType = 0
BlurPreview = 16
MagickLocaleOptions = 39
SemiExpandedStretch = 6
EdgeInMorphology = 13
RepeatSpread = 3
SaturationPreview = 5
ParzenFilter = 18
MonitorWarning = 385
OverCompositeOp = 40
DXT5Compression = 5
UndefinedColorInterpolate = 0
PNGInterlace = 7
PlaneInterlace = 3
MagickQuantumFormatOptions = 56
QuantumPixel = 6
UndefinedKernel = 0
ConcatenateMode = 3
MagickCompressOptions = 11
ModuleError = 455
BlurCompositeOp = 57
GradientReference = 1
FloydSteinbergDitherMethod = 3
TrueColorMatteType = 7
BGRAQuantum = 16
PolynomialDistortion = 8
FileOpenFatalError = 730
RGBAQuantum = 15
PolylinePrimitive = 8
UltraExpandedStretch = 9
MagickResolutionOptions = 57
OilPaintPreview = 27
SouthWestGravity = 7
TrimBoundsLayer = 16
DisposeLayer = 5
UserDefinedKernel = 33
CopyBlackCompositeOp = 11
SaturationIntent = 1
NoInterlace = 1
RollPreview = 3
OptimizePlusLayer = 8
TopLeftOrientation = 1
ShapeAlphaChannel = 9
ThresholdBlackEvaluateOperator = 16
PolicyEvent = 2048
YNegative = 64
DissolveCompositeOp = 28
SigmaValue = 8
YIQColorspace = 9
TransparentColorspace = 3
ImageTransmitType = 4
UndefinedPolicyDomain = 0
ExceptionEvent = 256
PeakSignalToNoiseRatioMetric = 6
BottomHatMorphology = 17
DarkenCompositeOp = 20
DstOverCompositeOp = 25
ErrorException = 400
SaturateCompositeOp = 44
JPEG2000Compression = 9
UndefinedFunction = 0
ShepardsDistortion = 14
MagickStorageOptions = 60
MagickFunctionOptions = 28
MultiplicativeGaussianNoise = 3
LoGKernel = 4
MiterJoin = 1
BlueQuantum = 3
ShadePreview = 21
LinearDodgeCompositeOp = 61
TrueAlphaChannel = 64
DstInCompositeOp = 23
UndefinedCap = 0
UndefinedMethod = 0
UndefinedNoise = 0
PaletteBilevelMatteType = 11
SplineInterpolatePixel = 8
BarrelDistortion = 12
CoderFatalError = 750
BlackChannel = 32
NearestNeighborInterpolatePixel = 7
MagickDataTypeOptions = 13
PointPrimitive = 1
WarningException = 300
OptimizeTransLayer = 9
MagickPrimitiveOptions = 55
CopyGreenCompositeOp = 15
PathPrimitive = 15
RunningTimerState = 2
GammaPreview = 7
HanningFilter = 5
MagickImageListOptions = 30
LaplacianNoiseEvaluateOperator = 20
WandEvent = 32768
TypeWarning = 305
QuadraticFilter = 9
AffineProjectionDistortion = 2
SharpenPreview = 15
HueCompositeOp = 31
NoneDispose = 1
MagickPolicyRightsOptions = 53
EncoderThreadSupport = 2
PathPolicyDomain = 4
UndefinedInterpolatePixel = 0
MagickModuleOptions = 47
UndefinedFormatType = 0
DelegateError = 415
SrcCompositeOp = 48
ZipCompression = 13
UnrecognizedDispose = 0
RedChannel = 1
RemoveZeroLayer = 11
DXT3Compression = 4
RandomNoise = 7
SobelKernel = 8
NoDecoration = 1
ConfigureError = 495
DefaultChannels = 295
MagickOrientationOptions = 50
RoundCap = 2
ReadPolicyRights = 1
NoValidate = 0
ObliqueStyle = 3
NonZeroRule = 2
X11Event = 65536
DiskResource = 2
MirrorVirtualPixelMethod = 5
ThinDiagonalsKernel = 24
MagickAlphaOptions = 1
CbYCrAQuantum = 24
ImageFatalError = 765
KirschKernel = 13
UndefinedOrientation = 0
ModulusAddCompositeOp = 2
LinePrimitive = 2
WhiteVirtualPixelMethod = 12
MagickDirectionOptions = 17
UndefinedAlphaChannel = 0
MultiplyEvaluateOperator = 7
BlobEvent = 4
NoCompliance = 0
MergeLayer = 13
SolarizePreview = 20
CopyYellowCompositeOp = 19
SentinelFilter = 22
UndefinedColorspace = 0
GrayPadQuantum = 20
QuantizePreview = 11
TextPrimitive = 13
MagickKernelOptions = 34
UndefinedPath = 0
ShortPixel = 7
CosineEvaluateOperator = 24
LanczosFilter = 13
LinearGradient = 1
BilinearForwardDistortion = 6
LuminizeCompositeOp = 35
UndefinedCompression = 0
HWBColorspace = 16
MagickCommandOptions = 9
FilterInterpolatePixel = 4
MagickPolicyOptions = 51
DeactivateAlphaChannel = 4
BlobError = 435
ModulusSubtractCompositeOp = 52
ColorDodgeCompositeOp = 9
MagickImageCoderModule = 0
YCCColorspace = 8
MagentaChannel = 2
HeadPath = 3
RobertsKernel = 10
MagickMethodOptions = 43
UndefinedPathUnits = 0
GrayscaleType = 2
IndexQuantum = 11
TypeFatalError = 705
ColorPrimitive = 11
FormatsInMemoryValidate = 8
ThreadResource = 6
ConvexHullKernel = 28
MagickClassOptions = 4
CometKernel = 6
MonitorFatalError = 785
NorthGravity = 2
MeanAbsoluteErrorMetric = 2
IOMode = 2
UndefinedLayer = 0
ChangeMaskCompositeOp = 6
EllipsePrimitive = 6
VerticalTileEdgeVirtualPixelMethod = 16
UndefinedInterlace = 0
MagickEndianOptions = 21
DilateMorphology = 4
SubtractEvaluateOperator = 11
PsiNegative = 64
XPMCompliance = 4
NormalStretch = 1
UndefinedReference = 0
AbsoluteErrorMetric = 1
TailPath = 4
B44Compression = 17
ReflectSpread = 2
WelshFilter = 17
PolynomialFunction = 1
XServerWarning = 380
UniformNoiseEvaluateOperator = 23
CoderError = 450
LineInterlace = 2
MagickFormatOptions = 27
GrayQuantum = 8
LongPixel = 5
UnframeMode = 2
DistortCompositeOp = 56
OpacityChannel = 8
CompareClearLayer = 3
RectangleKernel = 16
TrueColorType = 6
DitherVirtualPixelMethod = 3
DecimalValue = 262144
EuclideanKernel = 32
MagickColorspaceOptions = 8
MagickColorOptions = 7
EastGravity = 6
UndefinedQuantumAlpha = 0
CompareOverlayLayer = 4
ColorizeCompositeOp = 10
ShearPreview = 2
MagickFontOptions = 25
SetAlphaChannel = 8
BlackQuantum = 2
ThresholdEvaluateOperator = 15
HermiteFilter = 4
UndefinedEndian = 0
LeftTopOrientation = 5
DisplaceCompositeOp = 27
HeightValue = 8
PeaksKernel = 21
StreamTransmitType = 3
PeakAbsoluteErrorMetric = 5
PixelsPerCentimeterResolution = 2
MagickMagicOptions = 42
CanonicalPath = 8
MagickTrue = 1
TopHatMorphology = 16
BartlettFilter = 21
ReplaceCompositeOp = 43
JPEGCompression = 8
MagickMetricOptions = 44
CMYKOQuantum = 25
JPEGInterlace = 6
MagickSparseColorOptions = 59
AnyStretch = 10
GaussianNoise = 2
DoGKernel = 3
WandError = 470
PinLightCompositeOp = 60
AllChannels = 47
WriteMode = 1
UndefinedJoin = 0
ButtCap = 1
EvenOddRule = 1
MeshInterpolatePixel = 6
AllValidate = 2147483647
OptimizeType = 10
VoronoiColorInterpolate = 15
YellowQuantum = 19
DePolarDistortion = 11
CacheFatalError = 745
NorthWestGravity = 1
YCbCrColorspace = 7
SpiffPreview = 8
UndefinedAlign = 0
TileVirtualPixelMethod = 7
MagickConfigureOptions = 12
MissingDelegateError = 420
UndefinedEvents = 0
StaticGravity = 10
PseudoClass = 2
UndefinedException = 0
CopyCyanCompositeOp = 14
RelativeIntent = 4
ImagePrimitive = 14
ResourcePolicyDomain = 5
MagickListOptions = 38
StoppedTimerState = 1
MattePrimitive = 12
MagickGravityOptions = 29
UserSpaceOnUse = 2
MagickFilterOptions = 24
CondensedStretch = 4
ImpulseNoiseEvaluateOperator = 19
UserEvent = 16384
SouthGravity = 8
AffineDistortion = 1
StreamWarning = 340
XNegative = 32
BilinearReverseDistortion = 7
UndefinedDispose = 0
DecoderThreadSupport = 1
GIFInterlace = 5
SegmentPreview = 23
NormalizeValue = 8192
MagickStretchOptions = 61
MatteChannel = 8
OptionError = 410
SrcAtopCompositeOp = 47
RLECompression = 12
ReplaceMethod = 2
MeanSquaredErrorMetric = 4
MagickThresholdOptions = 63
SrcOverCompositeOp = 51
ConstantVirtualPixelMethod = 2
PoissonNoise = 6
UndefinedRegistryType = 0
LaplacianKernel = 7
UndefinedDecoration = 0
PolicyWarning = 399
RegistryError = 490
SyncChannels = 256
ScaleRotateTranslateDistortion = 3
SquareCap = 3
NoPolicyRights = 0
SincFilter = 15
UndefinedValidate = 0
FloodfillMethod = 3
MagickInterlaceOptions = 32
AreaResource = 1
ChiNegative = 128
CornersKernel = 23
CloseIntensityMorphology = 11
MagickAlignOptions = 0
CbYCrQuantum = 23
SentinelDistortion = 15
NoCompositeOp = 1
GrayVirtualPixelMethod = 11
MagickDelegateOptions = 16
ErodeMorphology = 3
MinEvaluateOperator = 6
AnnotateEvent = 2
BilinearDistortion = 6
OptionWarning = 310
CompositeLayer = 12
CopyRedCompositeOp = 18
GrayscalePreview = 10
DeprecateEvent = 64
MagickInterpolateOptions = 33
FillToBorderMethod = 4
DistanceMorphology = 7
MitchellFilter = 12
UndefinedGradient = 0
PerspectiveProjectionDistortion = 5
ModuleWarning = 355
LinearLightCompositeOp = 34
HSLColorspace = 15
AllValues = 2147483647
BilinearInterpolatePixel = 3
MagickFontsOptions = 26
GrayAlphaQuantum = 7
UndefinedPixel = 0
FileOpenError = 430
SpreadPreview = 19
Pxr24Compression = 16
GreenChannel = 2
X11Compliance = 2
MagickVirtualPixelOptions = 66
PowEvaluateOperator = 13
PrewittKernel = 11
LineThroughDecoration = 4
BilevelType = 1
ResourceLimitFatalError = 700
UndefinedChannel = 0
ConvertValidate = 4
MemoryResource = 5
LessValue = 16384
RidgesKernel = 27
MagickChannelOptions = 3
XServerFatalError = 780
EdgeVirtualPixelMethod = 4
ManhattanKernel = 31
BumpmapCompositeOp = 5
ArcPrimitive = 5
HorizontalTileEdgeVirtualPixelMethod = 15
GreaterValue = 32768
MagickDitherOptions = 20
CopyAlphaChannel = 3
AlphaQuantum = 1
SetEvaluateOperator = 10
ConfigureEvent = 32
XValue = 1
UndefinedStretch = 0
BottomLeftOrientation = 4
ReduceNoisePreview = 13
DstCompositeOp = 22
XiValue = 1
LogColorspace = 21
StreamValidate = 256
RingKernel = 20
AddNoisePreview = 14
UndefinedMetric = 0
MagickLineJoinOptions = 37
UndefinedResolution = 0
MeanEvaluateOperator = 27
PsiValue = 2
Rec709YCbCrColorspace = 20
PadSpread = 1
CyanQuantum = 6
RandomWarning = 375
MultiplyCompositeOp = 38
DXT1Compression = 3
Rec709LumaColorspace = 19
SystemPolicyDomain = 6
FloatingPointQuantumFormat = 1
MagickPreviewOptions = 54
ObjectBoundingBox = 3
UndefinedIntent = 0
FrameMode = 1
DivideCompositeOp = 55
LineJunctionsKernel = 26
RGBPadQuantum = 21
IntegerInterpolatePixel = 5
SquareKernel = 15
MissingDelegateFatalError = 720
PoissonNoiseEvaluateOperator = 22
AllEvents = 2147483647
ExpandedStretch = 7
PolicyFatalError = 799
CenterGravity = 5
FilterPolicyDomain = 3
PolygonPrimitive = 9
MagickImageFilterModule = 1
ResetAlphaChannel = 7
class N14pthread_cond_t4DOT_17E(Structure):
    pass
N14pthread_cond_t4DOT_17E._fields_ = [
    ('__lock', c_int),
    ('__futex', c_uint),
    ('__total_seq', c_ulonglong),
    ('__wakeup_seq', c_ulonglong),
    ('__woken_seq', c_ulonglong),
    ('__mutex', c_void_p),
    ('__nwaiters', c_uint),
    ('__broadcast_seq', c_uint),
]
class N16pthread_rwlock_t4DOT_20E(Structure):
    pass
N16pthread_rwlock_t4DOT_20E._fields_ = [
    ('__lock', c_int),
    ('__nr_readers', c_uint),
    ('__readers_wakeup', c_uint),
    ('__writer_wakeup', c_uint),
    ('__nr_readers_queued', c_uint),
    ('__nr_writers_queued', c_uint),
    ('__writer', c_int),
    ('__shared', c_int),
    ('__pad1', c_ulong),
    ('__pad2', c_ulong),
    ('__flags', c_uint),
]
class N4wait3DOT_6E(Structure):
    pass
N4wait3DOT_6E._fields_ = [
    ('__w_termsig', c_uint, 7),
    ('__w_coredump', c_uint, 1),
    ('__w_retcode', c_uint, 8),
    ('', c_uint, 16),
]
class N4wait3DOT_7E(Structure):
    pass
N4wait3DOT_7E._fields_ = [
    ('__w_stopval', c_uint, 8),
    ('__w_stopsig', c_uint, 8),
    ('', c_uint, 16),
]
class _IO_FILE(Structure):
    pass
FILE = _IO_FILE
class N11__mbstate_t3DOT_2E(Union):
    pass
N11__mbstate_t3DOT_2E._fields_ = [
    ('__wch', c_uint),
    ('__wchb', c_char * 4),
]

# values for enumeration 'MagickBooleanType'
MagickBooleanType = c_int # enum
class _Image(Structure):
    pass
Image = _Image
class KernelInfo(Structure):
    pass
class _ExceptionInfo(Structure):
    pass
ExceptionInfo = _ExceptionInfo
AccelerateConvolveImage = _lib.AccelerateConvolveImage
AccelerateConvolveImage.restype = MagickBooleanType
AccelerateConvolveImage.argtypes = [POINTER(Image), POINTER(KernelInfo), POINTER(Image), POINTER(ExceptionInfo)]
class _ImageInfo(Structure):
    pass
ImageInfo = _ImageInfo
AnimateImages = _lib.AnimateImages
AnimateImages.restype = MagickBooleanType
AnimateImages.argtypes = [POINTER(ImageInfo), POINTER(Image)]
class _DrawInfo(Structure):
    pass
DrawInfo = _DrawInfo
AnnotateImage = _lib.AnnotateImage
AnnotateImage.restype = MagickBooleanType
AnnotateImage.argtypes = [POINTER(Image), POINTER(DrawInfo)]
class _TypeMetric(Structure):
    pass
TypeMetric = _TypeMetric
GetMultilineTypeMetrics = _lib.GetMultilineTypeMetrics
GetMultilineTypeMetrics.restype = MagickBooleanType
GetMultilineTypeMetrics.argtypes = [POINTER(Image), POINTER(DrawInfo), POINTER(TypeMetric)]
GetTypeMetrics = _lib.GetTypeMetrics
GetTypeMetrics.restype = MagickBooleanType
GetTypeMetrics.argtypes = [POINTER(Image), POINTER(DrawInfo), POINTER(TypeMetric)]
__ssize_t = c_long
ssize_t = __ssize_t
FormatMagickCaption = _lib.FormatMagickCaption
FormatMagickCaption.restype = ssize_t
FormatMagickCaption.argtypes = [POINTER(Image), POINTER(DrawInfo), POINTER(TypeMetric), POINTER(STRING)]
GetNextImageArtifact = _lib.GetNextImageArtifact
GetNextImageArtifact.restype = STRING
GetNextImageArtifact.argtypes = [POINTER(Image)]
RemoveImageArtifact = _lib.RemoveImageArtifact
RemoveImageArtifact.restype = STRING
RemoveImageArtifact.argtypes = [POINTER(Image), STRING]
GetImageArtifact = _lib.GetImageArtifact
GetImageArtifact.restype = STRING
GetImageArtifact.argtypes = [POINTER(Image), STRING]
CloneImageArtifacts = _lib.CloneImageArtifacts
CloneImageArtifacts.restype = MagickBooleanType
CloneImageArtifacts.argtypes = [POINTER(Image), POINTER(Image)]
DefineImageArtifact = _lib.DefineImageArtifact
DefineImageArtifact.restype = MagickBooleanType
DefineImageArtifact.argtypes = [POINTER(Image), STRING]
DeleteImageArtifact = _lib.DeleteImageArtifact
DeleteImageArtifact.restype = MagickBooleanType
DeleteImageArtifact.argtypes = [POINTER(Image), STRING]
SetImageArtifact = _lib.SetImageArtifact
SetImageArtifact.restype = MagickBooleanType
SetImageArtifact.argtypes = [POINTER(Image), STRING, STRING]
DestroyImageArtifacts = _lib.DestroyImageArtifacts
DestroyImageArtifacts.restype = None
DestroyImageArtifacts.argtypes = [POINTER(Image)]
ResetImageArtifactIterator = _lib.ResetImageArtifactIterator
ResetImageArtifactIterator.restype = None
ResetImageArtifactIterator.argtypes = [POINTER(Image)]

# values for enumeration 'ImageType'
ImageType = c_int # enum
GetImageType = _lib.GetImageType
GetImageType.restype = ImageType
GetImageType.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
IsGrayImage = _lib.IsGrayImage
IsGrayImage.restype = MagickBooleanType
IsGrayImage.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
IsMonochromeImage = _lib.IsMonochromeImage
IsMonochromeImage.restype = MagickBooleanType
IsMonochromeImage.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
IsOpaqueImage = _lib.IsOpaqueImage
IsOpaqueImage.restype = MagickBooleanType
IsOpaqueImage.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]

# values for enumeration 'ChannelType'
ChannelType = c_int # enum
size_t = c_ulong
SetImageChannelDepth = _lib.SetImageChannelDepth
SetImageChannelDepth.restype = MagickBooleanType
SetImageChannelDepth.argtypes = [POINTER(Image), ChannelType, size_t]
SetImageDepth = _lib.SetImageDepth
SetImageDepth.restype = MagickBooleanType
SetImageDepth.argtypes = [POINTER(Image), size_t]
class _RectangleInfo(Structure):
    pass
RectangleInfo = _RectangleInfo
GetImageBoundingBox = _lib.GetImageBoundingBox
GetImageBoundingBox.restype = RectangleInfo
GetImageBoundingBox.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
GetImageChannelDepth = _lib.GetImageChannelDepth
GetImageChannelDepth.restype = size_t
GetImageChannelDepth.argtypes = [POINTER(Image), ChannelType, POINTER(ExceptionInfo)]
GetImageDepth = _lib.GetImageDepth
GetImageDepth.restype = size_t
GetImageDepth.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
GetImageQuantumDepth = _lib.GetImageQuantumDepth
GetImageQuantumDepth.restype = size_t
GetImageQuantumDepth.argtypes = [POINTER(Image), MagickBooleanType]

# values for enumeration 'MapMode'
MapMode = c_int # enum
GetBlobFileHandle = _lib.GetBlobFileHandle
GetBlobFileHandle.restype = POINTER(FILE)
GetBlobFileHandle.argtypes = [POINTER(Image)]
BlobToImage = _lib.BlobToImage
BlobToImage.restype = POINTER(Image)
BlobToImage.argtypes = [POINTER(ImageInfo), c_void_p, size_t, POINTER(ExceptionInfo)]
PingBlob = _lib.PingBlob
PingBlob.restype = POINTER(Image)
PingBlob.argtypes = [POINTER(ImageInfo), c_void_p, size_t, POINTER(ExceptionInfo)]
BlobToFile = _lib.BlobToFile
BlobToFile.restype = MagickBooleanType
BlobToFile.argtypes = [STRING, c_void_p, size_t, POINTER(ExceptionInfo)]
FileToImage = _lib.FileToImage
FileToImage.restype = MagickBooleanType
FileToImage.argtypes = [POINTER(Image), STRING]
GetBlobError = _lib.GetBlobError
GetBlobError.restype = MagickBooleanType
GetBlobError.argtypes = [POINTER(Image)]
ImageToFile = _lib.ImageToFile
ImageToFile.restype = MagickBooleanType
ImageToFile.argtypes = [POINTER(Image), STRING, POINTER(ExceptionInfo)]
InjectImageBlob = _lib.InjectImageBlob
InjectImageBlob.restype = MagickBooleanType
InjectImageBlob.argtypes = [POINTER(ImageInfo), POINTER(Image), POINTER(Image), STRING, POINTER(ExceptionInfo)]
IsBlobExempt = _lib.IsBlobExempt
IsBlobExempt.restype = MagickBooleanType
IsBlobExempt.argtypes = [POINTER(Image)]
IsBlobSeekable = _lib.IsBlobSeekable
IsBlobSeekable.restype = MagickBooleanType
IsBlobSeekable.argtypes = [POINTER(Image)]
IsBlobTemporary = _lib.IsBlobTemporary
IsBlobTemporary.restype = MagickBooleanType
IsBlobTemporary.argtypes = [POINTER(Image)]
MagickSizeType = c_ulonglong
GetBlobSize = _lib.GetBlobSize
GetBlobSize.restype = MagickSizeType
GetBlobSize.argtypes = [POINTER(Image)]
StreamHandler = CFUNCTYPE(size_t, POINTER(Image), c_void_p, size_t)
GetBlobStreamHandler = _lib.GetBlobStreamHandler
GetBlobStreamHandler.restype = StreamHandler
GetBlobStreamHandler.argtypes = [POINTER(Image)]
FileToBlob = _lib.FileToBlob
FileToBlob.restype = POINTER(c_ubyte)
FileToBlob.argtypes = [STRING, size_t, POINTER(size_t), POINTER(ExceptionInfo)]
GetBlobStreamData = _lib.GetBlobStreamData
GetBlobStreamData.restype = POINTER(c_ubyte)
GetBlobStreamData.argtypes = [POINTER(Image)]
ImageToBlob = _lib.ImageToBlob
ImageToBlob.restype = POINTER(c_ubyte)
ImageToBlob.argtypes = [POINTER(ImageInfo), POINTER(Image), POINTER(size_t), POINTER(ExceptionInfo)]
ImagesToBlob = _lib.ImagesToBlob
ImagesToBlob.restype = POINTER(c_ubyte)
ImagesToBlob.argtypes = [POINTER(ImageInfo), POINTER(Image), POINTER(size_t), POINTER(ExceptionInfo)]
DestroyBlob = _lib.DestroyBlob
DestroyBlob.restype = None
DestroyBlob.argtypes = [POINTER(Image)]
DuplicateBlob = _lib.DuplicateBlob
DuplicateBlob.restype = None
DuplicateBlob.argtypes = [POINTER(Image), POINTER(Image)]
SetBlobExempt = _lib.SetBlobExempt
SetBlobExempt.restype = None
SetBlobExempt.argtypes = [POINTER(Image), MagickBooleanType]

# values for enumeration 'VirtualPixelMethod'
VirtualPixelMethod = c_int # enum
class _CacheView(Structure):
    pass
CacheView = _CacheView

# values for enumeration 'ClassType'
ClassType = c_int # enum
GetCacheViewStorageClass = _lib.GetCacheViewStorageClass
GetCacheViewStorageClass.restype = ClassType
GetCacheViewStorageClass.argtypes = [POINTER(CacheView)]

# values for enumeration 'ColorspaceType'
sRGBColorspace = 13
ColorspaceType = c_int # enum
GetCacheViewColorspace = _lib.GetCacheViewColorspace
GetCacheViewColorspace.restype = ColorspaceType
GetCacheViewColorspace.argtypes = [POINTER(CacheView)]
Quantum = c_ushort
IndexPacket = Quantum
GetCacheViewVirtualIndexQueue = _lib.GetCacheViewVirtualIndexQueue
GetCacheViewVirtualIndexQueue.restype = POINTER(IndexPacket)
GetCacheViewVirtualIndexQueue.argtypes = [POINTER(CacheView)]
class _PixelPacket(Structure):
    pass
PixelPacket = _PixelPacket
GetCacheViewVirtualPixels = _lib.GetCacheViewVirtualPixels
GetCacheViewVirtualPixels.restype = POINTER(PixelPacket)
GetCacheViewVirtualPixels.argtypes = [POINTER(CacheView), ssize_t, ssize_t, size_t, size_t, POINTER(ExceptionInfo)]
GetCacheViewVirtualPixelQueue = _lib.GetCacheViewVirtualPixelQueue
GetCacheViewVirtualPixelQueue.restype = POINTER(PixelPacket)
GetCacheViewVirtualPixelQueue.argtypes = [POINTER(CacheView)]
GetCacheViewException = _lib.GetCacheViewException
GetCacheViewException.restype = POINTER(ExceptionInfo)
GetCacheViewException.argtypes = [POINTER(CacheView)]
GetCacheViewAuthenticIndexQueue = _lib.GetCacheViewAuthenticIndexQueue
GetCacheViewAuthenticIndexQueue.restype = POINTER(IndexPacket)
GetCacheViewAuthenticIndexQueue.argtypes = [POINTER(CacheView)]
GetOneCacheViewVirtualPixel = _lib.GetOneCacheViewVirtualPixel
GetOneCacheViewVirtualPixel.restype = MagickBooleanType
GetOneCacheViewVirtualPixel.argtypes = [POINTER(CacheView), ssize_t, ssize_t, POINTER(PixelPacket), POINTER(ExceptionInfo)]
GetOneCacheViewVirtualMethodPixel = _lib.GetOneCacheViewVirtualMethodPixel
GetOneCacheViewVirtualMethodPixel.restype = MagickBooleanType
GetOneCacheViewVirtualMethodPixel.argtypes = [POINTER(CacheView), VirtualPixelMethod, ssize_t, ssize_t, POINTER(PixelPacket), POINTER(ExceptionInfo)]
GetOneCacheViewAuthenticPixel = _lib.GetOneCacheViewAuthenticPixel
GetOneCacheViewAuthenticPixel.restype = MagickBooleanType
GetOneCacheViewAuthenticPixel.argtypes = [POINTER(CacheView), ssize_t, ssize_t, POINTER(PixelPacket), POINTER(ExceptionInfo)]
SetCacheViewStorageClass = _lib.SetCacheViewStorageClass
SetCacheViewStorageClass.restype = MagickBooleanType
SetCacheViewStorageClass.argtypes = [POINTER(CacheView), ClassType]
SetCacheViewVirtualPixelMethod = _lib.SetCacheViewVirtualPixelMethod
SetCacheViewVirtualPixelMethod.restype = MagickBooleanType
SetCacheViewVirtualPixelMethod.argtypes = [POINTER(CacheView), VirtualPixelMethod]
SyncCacheViewAuthenticPixels = _lib.SyncCacheViewAuthenticPixels
SyncCacheViewAuthenticPixels.restype = MagickBooleanType
SyncCacheViewAuthenticPixels.argtypes = [POINTER(CacheView), POINTER(ExceptionInfo)]
GetCacheViewExtent = _lib.GetCacheViewExtent
GetCacheViewExtent.restype = MagickSizeType
GetCacheViewExtent.argtypes = [POINTER(CacheView)]
GetCacheViewAuthenticPixelQueue = _lib.GetCacheViewAuthenticPixelQueue
GetCacheViewAuthenticPixelQueue.restype = POINTER(PixelPacket)
GetCacheViewAuthenticPixelQueue.argtypes = [POINTER(CacheView)]
GetCacheViewAuthenticPixels = _lib.GetCacheViewAuthenticPixels
GetCacheViewAuthenticPixels.restype = POINTER(PixelPacket)
GetCacheViewAuthenticPixels.argtypes = [POINTER(CacheView), ssize_t, ssize_t, size_t, size_t, POINTER(ExceptionInfo)]
QueueCacheViewAuthenticPixels = _lib.QueueCacheViewAuthenticPixels
QueueCacheViewAuthenticPixels.restype = POINTER(PixelPacket)
QueueCacheViewAuthenticPixels.argtypes = [POINTER(CacheView), ssize_t, ssize_t, size_t, size_t, POINTER(ExceptionInfo)]
AcquireCacheView = _lib.AcquireCacheView
AcquireCacheView.restype = POINTER(CacheView)
AcquireCacheView.argtypes = [POINTER(Image)]
CloneCacheView = _lib.CloneCacheView
CloneCacheView.restype = POINTER(CacheView)
CloneCacheView.argtypes = [POINTER(CacheView)]
DestroyCacheView = _lib.DestroyCacheView
DestroyCacheView.restype = POINTER(CacheView)
DestroyCacheView.argtypes = [POINTER(CacheView)]
GetVirtualIndexQueue = _lib.GetVirtualIndexQueue
GetVirtualIndexQueue.restype = POINTER(IndexPacket)
GetVirtualIndexQueue.argtypes = [POINTER(Image)]
GetVirtualPixels = _lib.GetVirtualPixels
GetVirtualPixels.restype = POINTER(PixelPacket)
GetVirtualPixels.argtypes = [POINTER(Image), ssize_t, ssize_t, size_t, size_t, POINTER(ExceptionInfo)]
GetVirtualPixelQueue = _lib.GetVirtualPixelQueue
GetVirtualPixelQueue.restype = POINTER(PixelPacket)
GetVirtualPixelQueue.argtypes = [POINTER(Image)]
AcquirePixelCachePixels = _lib.AcquirePixelCachePixels
AcquirePixelCachePixels.restype = c_void_p
AcquirePixelCachePixels.argtypes = [POINTER(Image), POINTER(MagickSizeType), POINTER(ExceptionInfo)]
GetAuthenticIndexQueue = _lib.GetAuthenticIndexQueue
GetAuthenticIndexQueue.restype = POINTER(IndexPacket)
GetAuthenticIndexQueue.argtypes = [POINTER(Image)]
CacheComponentGenesis = _lib.CacheComponentGenesis
CacheComponentGenesis.restype = MagickBooleanType
CacheComponentGenesis.argtypes = []
class _MagickPixelPacket(Structure):
    pass
MagickPixelPacket = _MagickPixelPacket
GetOneVirtualMagickPixel = _lib.GetOneVirtualMagickPixel
GetOneVirtualMagickPixel.restype = MagickBooleanType
GetOneVirtualMagickPixel.argtypes = [POINTER(Image), ssize_t, ssize_t, POINTER(MagickPixelPacket), POINTER(ExceptionInfo)]
GetOneVirtualPixel = _lib.GetOneVirtualPixel
GetOneVirtualPixel.restype = MagickBooleanType
GetOneVirtualPixel.argtypes = [POINTER(Image), ssize_t, ssize_t, POINTER(PixelPacket), POINTER(ExceptionInfo)]
GetOneVirtualMethodPixel = _lib.GetOneVirtualMethodPixel
GetOneVirtualMethodPixel.restype = MagickBooleanType
GetOneVirtualMethodPixel.argtypes = [POINTER(Image), VirtualPixelMethod, ssize_t, ssize_t, POINTER(PixelPacket), POINTER(ExceptionInfo)]
GetOneAuthenticPixel = _lib.GetOneAuthenticPixel
GetOneAuthenticPixel.restype = MagickBooleanType
GetOneAuthenticPixel.argtypes = [POINTER(Image), ssize_t, ssize_t, POINTER(PixelPacket), POINTER(ExceptionInfo)]
MagickOffsetType = c_longlong
PersistPixelCache = _lib.PersistPixelCache
PersistPixelCache.restype = MagickBooleanType
PersistPixelCache.argtypes = [POINTER(Image), STRING, MagickBooleanType, POINTER(MagickOffsetType), POINTER(ExceptionInfo)]
SyncAuthenticPixels = _lib.SyncAuthenticPixels
SyncAuthenticPixels.restype = MagickBooleanType
SyncAuthenticPixels.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
GetImageExtent = _lib.GetImageExtent
GetImageExtent.restype = MagickSizeType
GetImageExtent.argtypes = [POINTER(Image)]
GetAuthenticPixels = _lib.GetAuthenticPixels
GetAuthenticPixels.restype = POINTER(PixelPacket)
GetAuthenticPixels.argtypes = [POINTER(Image), ssize_t, ssize_t, size_t, size_t, POINTER(ExceptionInfo)]
GetAuthenticPixelQueue = _lib.GetAuthenticPixelQueue
GetAuthenticPixelQueue.restype = POINTER(PixelPacket)
GetAuthenticPixelQueue.argtypes = [POINTER(Image)]
QueueAuthenticPixels = _lib.QueueAuthenticPixels
QueueAuthenticPixels.restype = POINTER(PixelPacket)
QueueAuthenticPixels.argtypes = [POINTER(Image), ssize_t, ssize_t, size_t, size_t, POINTER(ExceptionInfo)]
GetPixelCacheVirtualMethod = _lib.GetPixelCacheVirtualMethod
GetPixelCacheVirtualMethod.restype = VirtualPixelMethod
GetPixelCacheVirtualMethod.argtypes = [POINTER(Image)]
SetPixelCacheVirtualMethod = _lib.SetPixelCacheVirtualMethod
SetPixelCacheVirtualMethod.restype = VirtualPixelMethod
SetPixelCacheVirtualMethod.argtypes = [POINTER(Image), VirtualPixelMethod]
CacheComponentTerminus = _lib.CacheComponentTerminus
CacheComponentTerminus.restype = None
CacheComponentTerminus.argtypes = []
GetPixelCachePixels = _lib.GetPixelCachePixels
GetPixelCachePixels.restype = c_void_p
GetPixelCachePixels.argtypes = [POINTER(Image), POINTER(MagickSizeType), POINTER(ExceptionInfo)]
DecipherImage = _lib.DecipherImage
DecipherImage.restype = MagickBooleanType
DecipherImage.argtypes = [POINTER(Image), STRING, POINTER(ExceptionInfo)]
EncipherImage = _lib.EncipherImage
EncipherImage.restype = MagickBooleanType
EncipherImage.argtypes = [POINTER(Image), STRING, POINTER(ExceptionInfo)]
class _StringInfo(Structure):
    pass
StringInfo = _StringInfo
PasskeyDecipherImage = _lib.PasskeyDecipherImage
PasskeyDecipherImage.restype = MagickBooleanType
PasskeyDecipherImage.argtypes = [POINTER(Image), POINTER(StringInfo), POINTER(ExceptionInfo)]
PasskeyEncipherImage = _lib.PasskeyEncipherImage
PasskeyEncipherImage.restype = MagickBooleanType
PasskeyEncipherImage.argtypes = [POINTER(Image), POINTER(StringInfo), POINTER(ExceptionInfo)]
GetClientPath = _lib.GetClientPath
GetClientPath.restype = STRING
GetClientPath.argtypes = []
GetClientName = _lib.GetClientName
GetClientName.restype = STRING
GetClientName.argtypes = []
SetClientName = _lib.SetClientName
SetClientName.restype = STRING
SetClientName.argtypes = [STRING]
SetClientPath = _lib.SetClientPath
SetClientPath.restype = STRING
SetClientPath.argtypes = [STRING]
class _CoderInfo(Structure):
    pass
CoderInfo = _CoderInfo
GetCoderList = _lib.GetCoderList
GetCoderList.restype = POINTER(STRING)
GetCoderList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
GetCoderInfo = _lib.GetCoderInfo
GetCoderInfo.restype = POINTER(CoderInfo)
GetCoderInfo.argtypes = [STRING, POINTER(ExceptionInfo)]
GetCoderInfoList = _lib.GetCoderInfoList
GetCoderInfoList.restype = POINTER(POINTER(CoderInfo))
GetCoderInfoList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
CoderComponentGenesis = _lib.CoderComponentGenesis
CoderComponentGenesis.restype = MagickBooleanType
CoderComponentGenesis.argtypes = []
ListCoderInfo = _lib.ListCoderInfo
ListCoderInfo.restype = MagickBooleanType
ListCoderInfo.argtypes = [POINTER(FILE), POINTER(ExceptionInfo)]
CoderComponentTerminus = _lib.CoderComponentTerminus
CoderComponentTerminus.restype = None
CoderComponentTerminus.argtypes = []

# values for enumeration 'ComplianceType'
ComplianceType = c_int # enum
class _ColorInfo(Structure):
    pass
ColorInfo = _ColorInfo
class _ErrorInfo(Structure):
    pass
ErrorInfo = _ErrorInfo
GetColorList = _lib.GetColorList
GetColorList.restype = POINTER(STRING)
GetColorList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
GetColorInfo = _lib.GetColorInfo
GetColorInfo.restype = POINTER(ColorInfo)
GetColorInfo.argtypes = [STRING, POINTER(ExceptionInfo)]
GetColorInfoList = _lib.GetColorInfoList
GetColorInfoList.restype = POINTER(POINTER(ColorInfo))
GetColorInfoList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
ColorComponentGenesis = _lib.ColorComponentGenesis
ColorComponentGenesis.restype = MagickBooleanType
ColorComponentGenesis.argtypes = []
IsColorSimilar = _lib.IsColorSimilar
IsColorSimilar.restype = MagickBooleanType
IsColorSimilar.argtypes = [POINTER(Image), POINTER(PixelPacket), POINTER(PixelPacket)]
IsImageSimilar = _lib.IsImageSimilar
IsImageSimilar.restype = MagickBooleanType
IsImageSimilar.argtypes = [POINTER(Image), POINTER(Image), POINTER(ssize_t), POINTER(ssize_t), POINTER(ExceptionInfo)]
IsMagickColorSimilar = _lib.IsMagickColorSimilar
IsMagickColorSimilar.restype = MagickBooleanType
IsMagickColorSimilar.argtypes = [POINTER(MagickPixelPacket), POINTER(MagickPixelPacket)]
IsOpacitySimilar = _lib.IsOpacitySimilar
IsOpacitySimilar.restype = MagickBooleanType
IsOpacitySimilar.argtypes = [POINTER(Image), POINTER(PixelPacket), POINTER(PixelPacket)]
ListColorInfo = _lib.ListColorInfo
ListColorInfo.restype = MagickBooleanType
ListColorInfo.argtypes = [POINTER(FILE), POINTER(ExceptionInfo)]
QueryColorDatabase = _lib.QueryColorDatabase
QueryColorDatabase.restype = MagickBooleanType
QueryColorDatabase.argtypes = [STRING, POINTER(PixelPacket), POINTER(ExceptionInfo)]
QueryColorname = _lib.QueryColorname
QueryColorname.restype = MagickBooleanType
QueryColorname.argtypes = [POINTER(Image), POINTER(PixelPacket), ComplianceType, STRING, POINTER(ExceptionInfo)]
QueryMagickColor = _lib.QueryMagickColor
QueryMagickColor.restype = MagickBooleanType
QueryMagickColor.argtypes = [STRING, POINTER(MagickPixelPacket), POINTER(ExceptionInfo)]
QueryMagickColorname = _lib.QueryMagickColorname
QueryMagickColorname.restype = MagickBooleanType
QueryMagickColorname.argtypes = [POINTER(Image), POINTER(MagickPixelPacket), ComplianceType, STRING, POINTER(ExceptionInfo)]
ColorComponentTerminus = _lib.ColorComponentTerminus
ColorComponentTerminus.restype = None
ColorComponentTerminus.argtypes = []
ConcatenateColorComponent = _lib.ConcatenateColorComponent
ConcatenateColorComponent.restype = None
ConcatenateColorComponent.argtypes = [POINTER(MagickPixelPacket), ChannelType, ComplianceType, STRING]
GetColorTuple = _lib.GetColorTuple
GetColorTuple.restype = None
GetColorTuple.argtypes = [POINTER(MagickPixelPacket), MagickBooleanType, STRING]
AcquireImageColormap = _lib.AcquireImageColormap
AcquireImageColormap.restype = MagickBooleanType
AcquireImageColormap.argtypes = [POINTER(Image), size_t]
CycleColormapImage = _lib.CycleColormapImage
CycleColormapImage.restype = MagickBooleanType
CycleColormapImage.argtypes = [POINTER(Image), ssize_t]
SortColormapByIntensity = _lib.SortColormapByIntensity
SortColormapByIntensity.restype = MagickBooleanType
SortColormapByIntensity.argtypes = [POINTER(Image)]
RGBTransformImage = _lib.RGBTransformImage
RGBTransformImage.restype = MagickBooleanType
RGBTransformImage.argtypes = [POINTER(Image), ColorspaceType]
SetImageColorspace = _lib.SetImageColorspace
SetImageColorspace.restype = MagickBooleanType
SetImageColorspace.argtypes = [POINTER(Image), ColorspaceType]
TransformImageColorspace = _lib.TransformImageColorspace
TransformImageColorspace.restype = MagickBooleanType
TransformImageColorspace.argtypes = [POINTER(Image), ColorspaceType]
TransformRGBImage = _lib.TransformRGBImage
TransformRGBImage.restype = MagickBooleanType
TransformRGBImage.argtypes = [POINTER(Image), ColorspaceType]

# values for enumeration 'MetricType'
MetricType = c_int # enum
GetImageChannelDistortions = _lib.GetImageChannelDistortions
GetImageChannelDistortions.restype = POINTER(c_double)
GetImageChannelDistortions.argtypes = [POINTER(Image), POINTER(Image), MetricType, POINTER(ExceptionInfo)]
CompareImageChannels = _lib.CompareImageChannels
CompareImageChannels.restype = POINTER(Image)
CompareImageChannels.argtypes = [POINTER(Image), POINTER(Image), ChannelType, MetricType, POINTER(c_double), POINTER(ExceptionInfo)]
CompareImages = _lib.CompareImages
CompareImages.restype = POINTER(Image)
CompareImages.argtypes = [POINTER(Image), POINTER(Image), MetricType, POINTER(c_double), POINTER(ExceptionInfo)]
SimilarityImage = _lib.SimilarityImage
SimilarityImage.restype = POINTER(Image)
SimilarityImage.argtypes = [POINTER(Image), POINTER(Image), POINTER(RectangleInfo), POINTER(c_double), POINTER(ExceptionInfo)]
GetImageChannelDistortion = _lib.GetImageChannelDistortion
GetImageChannelDistortion.restype = MagickBooleanType
GetImageChannelDistortion.argtypes = [POINTER(Image), POINTER(Image), ChannelType, MetricType, POINTER(c_double), POINTER(ExceptionInfo)]
GetImageDistortion = _lib.GetImageDistortion
GetImageDistortion.restype = MagickBooleanType
GetImageDistortion.argtypes = [POINTER(Image), POINTER(Image), MetricType, POINTER(c_double), POINTER(ExceptionInfo)]
IsImagesEqual = _lib.IsImagesEqual
IsImagesEqual.restype = MagickBooleanType
IsImagesEqual.argtypes = [POINTER(Image), POINTER(Image)]

# values for enumeration 'CompositeOperator'
CompositeOperator = c_int # enum
CompositeImage = _lib.CompositeImage
CompositeImage.restype = MagickBooleanType
CompositeImage.argtypes = [POINTER(Image), CompositeOperator, POINTER(Image), ssize_t, ssize_t]
CompositeImageChannel = _lib.CompositeImageChannel
CompositeImageChannel.restype = MagickBooleanType
CompositeImageChannel.argtypes = [POINTER(Image), ChannelType, CompositeOperator, POINTER(Image), ssize_t, ssize_t]
TextureImage = _lib.TextureImage
TextureImage.restype = MagickBooleanType
TextureImage.argtypes = [POINTER(Image), POINTER(Image)]

# values for enumeration 'CompressionType'
CompressionType = c_int # enum
class _Ascii85Info(Structure):
    pass
Ascii85Info = _Ascii85Info
HuffmanDecodeImage = _lib.HuffmanDecodeImage
HuffmanDecodeImage.restype = MagickBooleanType
HuffmanDecodeImage.argtypes = [POINTER(Image)]
HuffmanEncodeImage = _lib.HuffmanEncodeImage
HuffmanEncodeImage.restype = MagickBooleanType
HuffmanEncodeImage.argtypes = [POINTER(ImageInfo), POINTER(Image), POINTER(Image)]
LZWEncodeImage = _lib.LZWEncodeImage
LZWEncodeImage.restype = MagickBooleanType
LZWEncodeImage.argtypes = [POINTER(Image), size_t, POINTER(c_ubyte)]
PackbitsEncodeImage = _lib.PackbitsEncodeImage
PackbitsEncodeImage.restype = MagickBooleanType
PackbitsEncodeImage.argtypes = [POINTER(Image), size_t, POINTER(c_ubyte)]
ZLIBEncodeImage = _lib.ZLIBEncodeImage
ZLIBEncodeImage.restype = MagickBooleanType
ZLIBEncodeImage.argtypes = [POINTER(Image), size_t, POINTER(c_ubyte)]
Ascii85Encode = _lib.Ascii85Encode
Ascii85Encode.restype = None
Ascii85Encode.argtypes = [POINTER(Image), c_ubyte]
Ascii85Flush = _lib.Ascii85Flush
Ascii85Flush.restype = None
Ascii85Flush.argtypes = [POINTER(Image)]
Ascii85Initialize = _lib.Ascii85Initialize
Ascii85Initialize.restype = None
Ascii85Initialize.argtypes = [POINTER(Image)]
class _ConfigureInfo(Structure):
    pass
ConfigureInfo = _ConfigureInfo
GetConfigureList = _lib.GetConfigureList
GetConfigureList.restype = POINTER(STRING)
GetConfigureList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
GetConfigureOption = _lib.GetConfigureOption
GetConfigureOption.restype = STRING
GetConfigureOption.argtypes = [STRING]
GetConfigureValue = _lib.GetConfigureValue
GetConfigureValue.restype = STRING
GetConfigureValue.argtypes = [POINTER(ConfigureInfo)]
GetConfigureInfo = _lib.GetConfigureInfo
GetConfigureInfo.restype = POINTER(ConfigureInfo)
GetConfigureInfo.argtypes = [STRING, POINTER(ExceptionInfo)]
GetConfigureInfoList = _lib.GetConfigureInfoList
GetConfigureInfoList.restype = POINTER(POINTER(ConfigureInfo))
GetConfigureInfoList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
class _LinkedListInfo(Structure):
    pass
LinkedListInfo = _LinkedListInfo
DestroyConfigureOptions = _lib.DestroyConfigureOptions
DestroyConfigureOptions.restype = POINTER(LinkedListInfo)
DestroyConfigureOptions.argtypes = [POINTER(LinkedListInfo)]
GetConfigurePaths = _lib.GetConfigurePaths
GetConfigurePaths.restype = POINTER(LinkedListInfo)
GetConfigurePaths.argtypes = [STRING, POINTER(ExceptionInfo)]
GetConfigureOptions = _lib.GetConfigureOptions
GetConfigureOptions.restype = POINTER(LinkedListInfo)
GetConfigureOptions.argtypes = [STRING, POINTER(ExceptionInfo)]
ConfigureComponentGenesis = _lib.ConfigureComponentGenesis
ConfigureComponentGenesis.restype = MagickBooleanType
ConfigureComponentGenesis.argtypes = []
ListConfigureInfo = _lib.ListConfigureInfo
ListConfigureInfo.restype = MagickBooleanType
ListConfigureInfo.argtypes = [POINTER(FILE), POINTER(ExceptionInfo)]
ConfigureComponentTerminus = _lib.ConfigureComponentTerminus
ConfigureComponentTerminus.restype = None
ConfigureComponentTerminus.argtypes = []

# values for enumeration 'StorageType'
StorageType = c_int # enum
ConstituteImage = _lib.ConstituteImage
ConstituteImage.restype = POINTER(Image)
ConstituteImage.argtypes = [size_t, size_t, STRING, StorageType, c_void_p, POINTER(ExceptionInfo)]
PingImage = _lib.PingImage
PingImage.restype = POINTER(Image)
PingImage.argtypes = [POINTER(ImageInfo), POINTER(ExceptionInfo)]
PingImages = _lib.PingImages
PingImages.restype = POINTER(Image)
PingImages.argtypes = [POINTER(ImageInfo), POINTER(ExceptionInfo)]
ReadImage = _lib.ReadImage
ReadImage.restype = POINTER(Image)
ReadImage.argtypes = [POINTER(ImageInfo), POINTER(ExceptionInfo)]
ReadImages = _lib.ReadImages
ReadImages.restype = POINTER(Image)
ReadImages.argtypes = [POINTER(ImageInfo), POINTER(ExceptionInfo)]
ReadInlineImage = _lib.ReadInlineImage
ReadInlineImage.restype = POINTER(Image)
ReadInlineImage.argtypes = [POINTER(ImageInfo), STRING, POINTER(ExceptionInfo)]
ConstituteComponentGenesis = _lib.ConstituteComponentGenesis
ConstituteComponentGenesis.restype = MagickBooleanType
ConstituteComponentGenesis.argtypes = []
WriteImage = _lib.WriteImage
WriteImage.restype = MagickBooleanType
WriteImage.argtypes = [POINTER(ImageInfo), POINTER(Image)]
WriteImages = _lib.WriteImages
WriteImages.restype = MagickBooleanType
WriteImages.argtypes = [POINTER(ImageInfo), POINTER(Image), STRING, POINTER(ExceptionInfo)]
ConstituteComponentTerminus = _lib.ConstituteComponentTerminus
ConstituteComponentTerminus.restype = None
ConstituteComponentTerminus.argtypes = []
class _FrameInfo(Structure):
    pass
FrameInfo = _FrameInfo
BorderImage = _lib.BorderImage
BorderImage.restype = POINTER(Image)
BorderImage.argtypes = [POINTER(Image), POINTER(RectangleInfo), POINTER(ExceptionInfo)]
FrameImage = _lib.FrameImage
FrameImage.restype = POINTER(Image)
FrameImage.argtypes = [POINTER(Image), POINTER(FrameInfo), POINTER(ExceptionInfo)]
RaiseImage = _lib.RaiseImage
RaiseImage.restype = MagickBooleanType
RaiseImage.argtypes = [POINTER(Image), POINTER(RectangleInfo), MagickBooleanType]
class _DelegateInfo(Structure):
    pass
DelegateInfo = _DelegateInfo
GetDelegateCommand = _lib.GetDelegateCommand
GetDelegateCommand.restype = STRING
GetDelegateCommand.argtypes = [POINTER(ImageInfo), POINTER(Image), STRING, STRING, POINTER(ExceptionInfo)]
GetDelegateList = _lib.GetDelegateList
GetDelegateList.restype = POINTER(STRING)
GetDelegateList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
GetDelegateCommands = _lib.GetDelegateCommands
GetDelegateCommands.restype = STRING
GetDelegateCommands.argtypes = [POINTER(DelegateInfo)]
GetDelegateInfo = _lib.GetDelegateInfo
GetDelegateInfo.restype = POINTER(DelegateInfo)
GetDelegateInfo.argtypes = [STRING, STRING, POINTER(ExceptionInfo)]
GetDelegateInfoList = _lib.GetDelegateInfoList
GetDelegateInfoList.restype = POINTER(POINTER(DelegateInfo))
GetDelegateInfoList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
GetDelegateMode = _lib.GetDelegateMode
GetDelegateMode.restype = ssize_t
GetDelegateMode.argtypes = [POINTER(DelegateInfo)]
DelegateComponentGenesis = _lib.DelegateComponentGenesis
DelegateComponentGenesis.restype = MagickBooleanType
DelegateComponentGenesis.argtypes = []
GetDelegateThreadSupport = _lib.GetDelegateThreadSupport
GetDelegateThreadSupport.restype = MagickBooleanType
GetDelegateThreadSupport.argtypes = [POINTER(DelegateInfo)]
InvokeDelegate = _lib.InvokeDelegate
InvokeDelegate.restype = MagickBooleanType
InvokeDelegate.argtypes = [POINTER(ImageInfo), POINTER(Image), STRING, STRING, POINTER(ExceptionInfo)]
ListDelegateInfo = _lib.ListDelegateInfo
ListDelegateInfo.restype = MagickBooleanType
ListDelegateInfo.argtypes = [POINTER(FILE), POINTER(ExceptionInfo)]
DelegateComponentTerminus = _lib.DelegateComponentTerminus
DelegateComponentTerminus.restype = None
DelegateComponentTerminus.argtypes = []

# values for enumeration 'MagickLayerMethod'
MagickLayerMethod = c_int # enum
ExtendedSignedIntegralType = MagickOffsetType
ExtendedUnsignedIntegralType = MagickSizeType
MagickRealType = c_double
ExtendedRationalType = MagickRealType
class _ViewInfo(Structure):
    pass
ViewInfo = _ViewInfo
MonitorHandler = CFUNCTYPE(MagickBooleanType, STRING, MagickOffsetType, MagickSizeType, POINTER(ExceptionInfo))
class _ImageAttribute(Structure):
    pass
ImageAttribute = _ImageAttribute
CloseCacheView = _lib.CloseCacheView
CloseCacheView.restype = POINTER(CacheView)
CloseCacheView.argtypes = [POINTER(CacheView)]
OpenCacheView = _lib.OpenCacheView
OpenCacheView.restype = POINTER(CacheView)
OpenCacheView.argtypes = [POINTER(Image)]
AllocateString = _lib.AllocateString
AllocateString.restype = STRING
AllocateString.argtypes = [STRING]
InterpretImageAttributes = _lib.InterpretImageAttributes
InterpretImageAttributes.restype = STRING
InterpretImageAttributes.argtypes = [POINTER(ImageInfo), POINTER(Image), STRING]
PostscriptGeometry = _lib.PostscriptGeometry
PostscriptGeometry.restype = STRING
PostscriptGeometry.argtypes = [STRING]
TranslateText = _lib.TranslateText
TranslateText.restype = STRING
TranslateText.argtypes = [POINTER(ImageInfo), POINTER(Image), STRING]
GetImageAttribute = _lib.GetImageAttribute
GetImageAttribute.restype = POINTER(ImageAttribute)
GetImageAttribute.argtypes = [POINTER(Image), STRING]
GetImageClippingPathAttribute = _lib.GetImageClippingPathAttribute
GetImageClippingPathAttribute.restype = POINTER(ImageAttribute)
GetImageClippingPathAttribute.argtypes = [POINTER(Image)]
GetNextImageAttribute = _lib.GetNextImageAttribute
GetNextImageAttribute.restype = POINTER(ImageAttribute)
GetNextImageAttribute.argtypes = [POINTER(Image)]
AcquireCacheViewIndexes = _lib.AcquireCacheViewIndexes
AcquireCacheViewIndexes.restype = POINTER(IndexPacket)
AcquireCacheViewIndexes.argtypes = [POINTER(CacheView)]
AcquireIndexes = _lib.AcquireIndexes
AcquireIndexes.restype = POINTER(IndexPacket)
AcquireIndexes.argtypes = [POINTER(Image)]
AcquirePixels = _lib.AcquirePixels
AcquirePixels.restype = POINTER(PixelPacket)
AcquirePixels.argtypes = [POINTER(Image)]
AcquireCacheViewPixels = _lib.AcquireCacheViewPixels
AcquireCacheViewPixels.restype = POINTER(PixelPacket)
AcquireCacheViewPixels.argtypes = [POINTER(CacheView), ssize_t, ssize_t, size_t, size_t, POINTER(ExceptionInfo)]
AcquireImagePixels = _lib.AcquireImagePixels
AcquireImagePixels.restype = POINTER(PixelPacket)
AcquireImagePixels.argtypes = [POINTER(Image), ssize_t, ssize_t, size_t, size_t, POINTER(ExceptionInfo)]
AllocateImage = _lib.AllocateImage
AllocateImage.restype = POINTER(Image)
AllocateImage.argtypes = [POINTER(ImageInfo)]
AverageImages = _lib.AverageImages
AverageImages.restype = POINTER(Image)
AverageImages.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
ExtractSubimageFromImage = _lib.ExtractSubimageFromImage
ExtractSubimageFromImage.restype = POINTER(Image)
ExtractSubimageFromImage.argtypes = [POINTER(Image), POINTER(Image), POINTER(ExceptionInfo)]
GetImageFromMagickRegistry = _lib.GetImageFromMagickRegistry
GetImageFromMagickRegistry.restype = POINTER(Image)
GetImageFromMagickRegistry.argtypes = [STRING, POINTER(ssize_t), POINTER(ExceptionInfo)]
GetImageList = _lib.GetImageList
GetImageList.restype = POINTER(Image)
GetImageList.argtypes = [POINTER(Image), ssize_t, POINTER(ExceptionInfo)]
GetNextImage = _lib.GetNextImage
GetNextImage.restype = POINTER(Image)
GetNextImage.argtypes = [POINTER(Image)]
GetPreviousImage = _lib.GetPreviousImage
GetPreviousImage.restype = POINTER(Image)
GetPreviousImage.argtypes = [POINTER(Image)]
FlattenImages = _lib.FlattenImages
FlattenImages.restype = POINTER(Image)
FlattenImages.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
MaximumImages = _lib.MaximumImages
MaximumImages.restype = POINTER(Image)
MaximumImages.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
MinimumImages = _lib.MinimumImages
MinimumImages.restype = POINTER(Image)
MinimumImages.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
MosaicImages = _lib.MosaicImages
MosaicImages.restype = POINTER(Image)
MosaicImages.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
PopImageList = _lib.PopImageList
PopImageList.restype = POINTER(Image)
PopImageList.argtypes = [POINTER(POINTER(Image))]
RecolorImage = _lib.RecolorImage
RecolorImage.restype = POINTER(Image)
RecolorImage.argtypes = [POINTER(Image), size_t, POINTER(c_double), POINTER(ExceptionInfo)]
ShiftImageList = _lib.ShiftImageList
ShiftImageList.restype = POINTER(Image)
ShiftImageList.argtypes = [POINTER(POINTER(Image))]
SpliceImageList = _lib.SpliceImageList
SpliceImageList.restype = POINTER(Image)
SpliceImageList.argtypes = [POINTER(Image), ssize_t, size_t, POINTER(Image), POINTER(ExceptionInfo)]
GetCacheViewIndexes = _lib.GetCacheViewIndexes
GetCacheViewIndexes.restype = POINTER(IndexPacket)
GetCacheViewIndexes.argtypes = [POINTER(CacheView)]
GetIndexes = _lib.GetIndexes
GetIndexes.restype = POINTER(IndexPacket)
GetIndexes.argtypes = [POINTER(Image)]
ValidateColormapIndex = _lib.ValidateColormapIndex
ValidateColormapIndex.restype = IndexPacket
ValidateColormapIndex.argtypes = [POINTER(Image), size_t]
GetImageGeometry = _lib.GetImageGeometry
GetImageGeometry.restype = c_int
GetImageGeometry.argtypes = [POINTER(Image), STRING, c_uint, POINTER(RectangleInfo)]
ParseImageGeometry = _lib.ParseImageGeometry
ParseImageGeometry.restype = c_int
ParseImageGeometry.argtypes = [STRING, POINTER(ssize_t), POINTER(ssize_t), POINTER(size_t), POINTER(size_t)]
GetImageListIndex = _lib.GetImageListIndex
GetImageListIndex.restype = ssize_t
GetImageListIndex.argtypes = [POINTER(Image)]

# values for enumeration 'RegistryType'
RegistryType = c_int # enum
SetMagickRegistry = _lib.SetMagickRegistry
SetMagickRegistry.restype = ssize_t
SetMagickRegistry.argtypes = [RegistryType, c_void_p, size_t, POINTER(ExceptionInfo)]
AcquireOneCacheViewPixel = _lib.AcquireOneCacheViewPixel
AcquireOneCacheViewPixel.restype = MagickBooleanType
AcquireOneCacheViewPixel.argtypes = [POINTER(CacheView), ssize_t, ssize_t, POINTER(PixelPacket), POINTER(ExceptionInfo)]
AcquireOneCacheViewVirtualPixel = _lib.AcquireOneCacheViewVirtualPixel
AcquireOneCacheViewVirtualPixel.restype = MagickBooleanType
AcquireOneCacheViewVirtualPixel.argtypes = [POINTER(CacheView), VirtualPixelMethod, ssize_t, ssize_t, POINTER(PixelPacket), POINTER(ExceptionInfo)]
class _QuantizeInfo(Structure):
    pass
QuantizeInfo = _QuantizeInfo
AffinityImage = _lib.AffinityImage
AffinityImage.restype = MagickBooleanType
AffinityImage.argtypes = [POINTER(QuantizeInfo), POINTER(Image), POINTER(Image)]
AffinityImages = _lib.AffinityImages
AffinityImages.restype = MagickBooleanType
AffinityImages.argtypes = [POINTER(QuantizeInfo), POINTER(Image), POINTER(Image)]
AllocateImageColormap = _lib.AllocateImageColormap
AllocateImageColormap.restype = MagickBooleanType
AllocateImageColormap.argtypes = [POINTER(Image), size_t]
ClipPathImage = _lib.ClipPathImage
ClipPathImage.restype = MagickBooleanType
ClipPathImage.argtypes = [POINTER(Image), STRING, MagickBooleanType]
CloneImageAttributes = _lib.CloneImageAttributes
CloneImageAttributes.restype = MagickBooleanType
CloneImageAttributes.argtypes = [POINTER(Image), POINTER(Image)]

# values for enumeration 'PaintMethod'
PaintMethod = c_int # enum
ColorFloodfillImage = _lib.ColorFloodfillImage
ColorFloodfillImage.restype = MagickBooleanType
ColorFloodfillImage.argtypes = [POINTER(Image), POINTER(DrawInfo), PixelPacket, ssize_t, ssize_t, PaintMethod]
DeleteImageAttribute = _lib.DeleteImageAttribute
DeleteImageAttribute.restype = MagickBooleanType
DeleteImageAttribute.argtypes = [POINTER(Image), STRING]
DeleteMagickRegistry = _lib.DeleteMagickRegistry
DeleteMagickRegistry.restype = MagickBooleanType
DeleteMagickRegistry.argtypes = [ssize_t]
DescribeImage = _lib.DescribeImage
DescribeImage.restype = MagickBooleanType
DescribeImage.argtypes = [POINTER(Image), POINTER(FILE), MagickBooleanType]
FormatImageAttribute = _lib.FormatImageAttribute
FormatImageAttribute.restype = MagickBooleanType
FormatImageAttribute.argtypes = [POINTER(Image), STRING, STRING]
class __va_list_tag(Structure):
    pass
FormatImageAttributeList = _lib.FormatImageAttributeList
FormatImageAttributeList.restype = MagickBooleanType
FormatImageAttributeList.argtypes = [POINTER(Image), STRING, STRING, POINTER(__va_list_tag)]
FuzzyColorCompare = _lib.FuzzyColorCompare
FuzzyColorCompare.restype = MagickBooleanType
FuzzyColorCompare.argtypes = [POINTER(Image), POINTER(PixelPacket), POINTER(PixelPacket)]
FuzzyOpacityCompare = _lib.FuzzyOpacityCompare
FuzzyOpacityCompare.restype = MagickBooleanType
FuzzyOpacityCompare.argtypes = [POINTER(Image), POINTER(PixelPacket), POINTER(PixelPacket)]
LevelImageColors = _lib.LevelImageColors
LevelImageColors.restype = MagickBooleanType
LevelImageColors.argtypes = [POINTER(Image), ChannelType, POINTER(MagickPixelPacket), POINTER(MagickPixelPacket), MagickBooleanType]
MagickMonitor = _lib.MagickMonitor
MagickMonitor.restype = MagickBooleanType
MagickMonitor.argtypes = [STRING, MagickOffsetType, MagickSizeType, c_void_p]
MapImage = _lib.MapImage
MapImage.restype = MagickBooleanType
MapImage.argtypes = [POINTER(Image), POINTER(Image), MagickBooleanType]
MapImages = _lib.MapImages
MapImages.restype = MagickBooleanType
MapImages.argtypes = [POINTER(Image), POINTER(Image), MagickBooleanType]
MatteFloodfillImage = _lib.MatteFloodfillImage
MatteFloodfillImage.restype = MagickBooleanType
MatteFloodfillImage.argtypes = [POINTER(Image), PixelPacket, Quantum, ssize_t, ssize_t, PaintMethod]
OpaqueImage = _lib.OpaqueImage
OpaqueImage.restype = MagickBooleanType
OpaqueImage.argtypes = [POINTER(Image), PixelPacket, PixelPacket]
PaintFloodfillImage = _lib.PaintFloodfillImage
PaintFloodfillImage.restype = MagickBooleanType
PaintFloodfillImage.argtypes = [POINTER(Image), ChannelType, POINTER(MagickPixelPacket), ssize_t, ssize_t, POINTER(DrawInfo), PaintMethod]
PaintOpaqueImage = _lib.PaintOpaqueImage
PaintOpaqueImage.restype = MagickBooleanType
PaintOpaqueImage.argtypes = [POINTER(Image), POINTER(MagickPixelPacket), POINTER(MagickPixelPacket)]
PaintOpaqueImageChannel = _lib.PaintOpaqueImageChannel
PaintOpaqueImageChannel.restype = MagickBooleanType
PaintOpaqueImageChannel.argtypes = [POINTER(Image), ChannelType, POINTER(MagickPixelPacket), POINTER(MagickPixelPacket)]
PaintTransparentImage = _lib.PaintTransparentImage
PaintTransparentImage.restype = MagickBooleanType
PaintTransparentImage.argtypes = [POINTER(Image), POINTER(MagickPixelPacket), Quantum]

# values for enumeration 'ExceptionType'
ExceptionType = c_int # enum
SetExceptionInfo = _lib.SetExceptionInfo
SetExceptionInfo.restype = MagickBooleanType
SetExceptionInfo.argtypes = [POINTER(ExceptionInfo), ExceptionType]
SetImageAttribute = _lib.SetImageAttribute
SetImageAttribute.restype = MagickBooleanType
SetImageAttribute.argtypes = [POINTER(Image), STRING, STRING]
SyncCacheViewPixels = _lib.SyncCacheViewPixels
SyncCacheViewPixels.restype = MagickBooleanType
SyncCacheViewPixels.argtypes = [POINTER(CacheView)]
SyncImagePixels = _lib.SyncImagePixels
SyncImagePixels.restype = MagickBooleanType
SyncImagePixels.argtypes = [POINTER(Image)]
TransparentImage = _lib.TransparentImage
TransparentImage.restype = MagickBooleanType
TransparentImage.argtypes = [POINTER(Image), PixelPacket, Quantum]
AcquireOneMagickPixel = _lib.AcquireOneMagickPixel
AcquireOneMagickPixel.restype = MagickPixelPacket
AcquireOneMagickPixel.argtypes = [POINTER(Image), ssize_t, ssize_t, POINTER(ExceptionInfo)]
GetMonitorHandler = _lib.GetMonitorHandler
GetMonitorHandler.restype = MonitorHandler
GetMonitorHandler.argtypes = []
SetMonitorHandler = _lib.SetMonitorHandler
SetMonitorHandler.restype = MonitorHandler
SetMonitorHandler.argtypes = [MonitorHandler]
SizeBlob = _lib.SizeBlob
SizeBlob.restype = MagickOffsetType
SizeBlob.argtypes = [POINTER(Image)]

# values for enumeration 'InterpolatePixelMethod'
InterpolatePixelMethod = c_int # enum
InterpolatePixelColor = _lib.InterpolatePixelColor
InterpolatePixelColor.restype = MagickPixelPacket
InterpolatePixelColor.argtypes = [POINTER(Image), POINTER(CacheView), InterpolatePixelMethod, c_double, c_double, POINTER(ExceptionInfo)]
MagickStatusType = c_uint
ParseSizeGeometry = _lib.ParseSizeGeometry
ParseSizeGeometry.restype = MagickStatusType
ParseSizeGeometry.argtypes = [POINTER(Image), STRING, POINTER(RectangleInfo)]
AcquireOnePixel = _lib.AcquireOnePixel
AcquireOnePixel.restype = PixelPacket
AcquireOnePixel.argtypes = [POINTER(Image), ssize_t, ssize_t, POINTER(ExceptionInfo)]
AcquireOneVirtualPixel = _lib.AcquireOneVirtualPixel
AcquireOneVirtualPixel.restype = PixelPacket
AcquireOneVirtualPixel.argtypes = [POINTER(Image), VirtualPixelMethod, ssize_t, ssize_t, POINTER(ExceptionInfo)]
GetCacheView = _lib.GetCacheView
GetCacheView.restype = POINTER(PixelPacket)
GetCacheView.argtypes = [POINTER(CacheView), ssize_t, ssize_t, size_t, size_t]
GetCacheViewPixels = _lib.GetCacheViewPixels
GetCacheViewPixels.restype = POINTER(PixelPacket)
GetCacheViewPixels.argtypes = [POINTER(CacheView), ssize_t, ssize_t, size_t, size_t]
GetImagePixels = _lib.GetImagePixels
GetImagePixels.restype = POINTER(PixelPacket)
GetImagePixels.argtypes = [POINTER(Image), ssize_t, ssize_t, size_t, size_t]
GetOnePixel = _lib.GetOnePixel
GetOnePixel.restype = PixelPacket
GetOnePixel.argtypes = [POINTER(Image), ssize_t, ssize_t]
GetPixels = _lib.GetPixels
GetPixels.restype = POINTER(PixelPacket)
GetPixels.argtypes = [POINTER(Image)]
SetCacheViewPixels = _lib.SetCacheViewPixels
SetCacheViewPixels.restype = POINTER(PixelPacket)
SetCacheViewPixels.argtypes = [POINTER(CacheView), ssize_t, ssize_t, size_t, size_t]
SetImagePixels = _lib.SetImagePixels
SetImagePixels.restype = POINTER(PixelPacket)
SetImagePixels.argtypes = [POINTER(Image), ssize_t, ssize_t, size_t, size_t]
GetImageListSize = _lib.GetImageListSize
GetImageListSize.restype = size_t
GetImageListSize.argtypes = [POINTER(Image)]

# values for enumeration 'QuantumType'
QuantumType = c_int # enum
PopImagePixels = _lib.PopImagePixels
PopImagePixels.restype = size_t
PopImagePixels.argtypes = [POINTER(Image), QuantumType, POINTER(c_ubyte)]
PushImagePixels = _lib.PushImagePixels
PushImagePixels.restype = size_t
PushImagePixels.argtypes = [POINTER(Image), QuantumType, POINTER(c_ubyte)]
ChannelImage = _lib.ChannelImage
ChannelImage.restype = c_uint
ChannelImage.argtypes = [POINTER(Image), ChannelType]
ChannelThresholdImage = _lib.ChannelThresholdImage
ChannelThresholdImage.restype = c_uint
ChannelThresholdImage.argtypes = [POINTER(Image), STRING]
DispatchImage = _lib.DispatchImage
DispatchImage.restype = c_uint
DispatchImage.argtypes = [POINTER(Image), ssize_t, ssize_t, size_t, size_t, STRING, StorageType, c_void_p, POINTER(ExceptionInfo)]
FuzzyColorMatch = _lib.FuzzyColorMatch
FuzzyColorMatch.restype = c_uint
FuzzyColorMatch.argtypes = [POINTER(PixelPacket), POINTER(PixelPacket), c_double]
GetNumberScenes = _lib.GetNumberScenes
GetNumberScenes.restype = c_uint
GetNumberScenes.argtypes = [POINTER(Image)]
GetMagickGeometry = _lib.GetMagickGeometry
GetMagickGeometry.restype = c_uint
GetMagickGeometry.argtypes = [STRING, POINTER(ssize_t), POINTER(ssize_t), POINTER(size_t), POINTER(size_t)]
IsSubimage = _lib.IsSubimage
IsSubimage.restype = c_uint
IsSubimage.argtypes = [STRING, c_uint]
PushImageList = _lib.PushImageList
PushImageList.restype = c_uint
PushImageList.argtypes = [POINTER(POINTER(Image)), POINTER(Image), POINTER(ExceptionInfo)]
QuantizationError = _lib.QuantizationError
QuantizationError.restype = c_uint
QuantizationError.argtypes = [POINTER(Image)]
RandomChannelThresholdImage = _lib.RandomChannelThresholdImage
RandomChannelThresholdImage.restype = c_uint
RandomChannelThresholdImage.argtypes = [POINTER(Image), STRING, STRING, POINTER(ExceptionInfo)]
SetImageList = _lib.SetImageList
SetImageList.restype = c_uint
SetImageList.argtypes = [POINTER(POINTER(Image)), POINTER(Image), ssize_t, POINTER(ExceptionInfo)]
TransformColorspace = _lib.TransformColorspace
TransformColorspace.restype = c_uint
TransformColorspace.argtypes = [POINTER(Image), ColorspaceType]
ThresholdImage = _lib.ThresholdImage
ThresholdImage.restype = c_uint
ThresholdImage.argtypes = [POINTER(Image), c_double]
ThresholdImageChannel = _lib.ThresholdImageChannel
ThresholdImageChannel.restype = c_uint
ThresholdImageChannel.argtypes = [POINTER(Image), STRING]
UnshiftImageList = _lib.UnshiftImageList
UnshiftImageList.restype = c_uint
UnshiftImageList.argtypes = [POINTER(POINTER(Image)), POINTER(Image), POINTER(ExceptionInfo)]
AcquireMemory = _lib.AcquireMemory
AcquireMemory.restype = c_void_p
AcquireMemory.argtypes = [size_t]
AllocateNextImage = _lib.AllocateNextImage
AllocateNextImage.restype = None
AllocateNextImage.argtypes = [POINTER(ImageInfo), POINTER(Image)]
CloneMemory = _lib.CloneMemory
CloneMemory.restype = c_void_p
CloneMemory.argtypes = [c_void_p, c_void_p, size_t]
DestroyImageAttributes = _lib.DestroyImageAttributes
DestroyImageAttributes.restype = None
DestroyImageAttributes.argtypes = [POINTER(Image)]
DestroyImages = _lib.DestroyImages
DestroyImages.restype = None
DestroyImages.argtypes = [POINTER(Image)]
DestroyMagick = _lib.DestroyMagick
DestroyMagick.restype = None
DestroyMagick.argtypes = []
DestroyMagickRegistry = _lib.DestroyMagickRegistry
DestroyMagickRegistry.restype = None
DestroyMagickRegistry.argtypes = []
GetConfigureBlob = _lib.GetConfigureBlob
GetConfigureBlob.restype = c_void_p
GetConfigureBlob.argtypes = [STRING, STRING, POINTER(size_t), POINTER(ExceptionInfo)]
GetMagickRegistry = _lib.GetMagickRegistry
GetMagickRegistry.restype = c_void_p
GetMagickRegistry.argtypes = [ssize_t, POINTER(RegistryType), POINTER(size_t), POINTER(ExceptionInfo)]
class _AffineMatrix(Structure):
    pass
AffineMatrix = _AffineMatrix
IdentityAffine = _lib.IdentityAffine
IdentityAffine.restype = None
IdentityAffine.argtypes = [POINTER(AffineMatrix)]
LiberateMemory = _lib.LiberateMemory
LiberateMemory.restype = None
LiberateMemory.argtypes = [POINTER(c_void_p)]
class SemaphoreInfo(Structure):
    pass
LiberateSemaphoreInfo = _lib.LiberateSemaphoreInfo
LiberateSemaphoreInfo.restype = None
LiberateSemaphoreInfo.argtypes = [POINTER(POINTER(SemaphoreInfo))]
FormatString = _lib.FormatString
FormatString.restype = None
FormatString.argtypes = [STRING, STRING]
FormatStringList = _lib.FormatStringList
FormatStringList.restype = None
FormatStringList.argtypes = [STRING, STRING, POINTER(__va_list_tag)]
HSLTransform = _lib.HSLTransform
HSLTransform.restype = None
HSLTransform.argtypes = [c_double, c_double, c_double, POINTER(Quantum), POINTER(Quantum), POINTER(Quantum)]
InitializeMagick = _lib.InitializeMagick
InitializeMagick.restype = None
InitializeMagick.argtypes = [STRING]
MagickIncarnate = _lib.MagickIncarnate
MagickIncarnate.restype = None
MagickIncarnate.argtypes = [STRING]
ReacquireMemory = _lib.ReacquireMemory
ReacquireMemory.restype = None
ReacquireMemory.argtypes = [POINTER(c_void_p), size_t]
ResetImageAttributeIterator = _lib.ResetImageAttributeIterator
ResetImageAttributeIterator.restype = None
ResetImageAttributeIterator.argtypes = [POINTER(Image)]
SetCacheThreshold = _lib.SetCacheThreshold
SetCacheThreshold.restype = None
SetCacheThreshold.argtypes = [size_t]
SetImage = _lib.SetImage
SetImage.restype = None
SetImage.argtypes = [POINTER(Image), Quantum]
Strip = _lib.Strip
Strip.restype = None
Strip.argtypes = [STRING]
TemporaryFilename = _lib.TemporaryFilename
TemporaryFilename.restype = None
TemporaryFilename.argtypes = [STRING]
TransformHSL = _lib.TransformHSL
TransformHSL.restype = None
TransformHSL.argtypes = [Quantum, Quantum, Quantum, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
DisplayImages = _lib.DisplayImages
DisplayImages.restype = MagickBooleanType
DisplayImages.argtypes = [POINTER(ImageInfo), POINTER(Image)]
RemoteDisplayCommand = _lib.RemoteDisplayCommand
RemoteDisplayCommand.restype = MagickBooleanType
RemoteDisplayCommand.argtypes = [POINTER(ImageInfo), STRING, STRING, POINTER(ExceptionInfo)]

# values for enumeration 'DistortImageMethod'
DistortImageMethod = c_int # enum

# values for enumeration 'SparseColorMethod'
SparseColorMethod = c_int # enum
DistortImage = _lib.DistortImage
DistortImage.restype = POINTER(Image)
DistortImage.argtypes = [POINTER(Image), DistortImageMethod, size_t, POINTER(c_double), MagickBooleanType, POINTER(ExceptionInfo)]
SparseColorImage = _lib.SparseColorImage
SparseColorImage.restype = POINTER(Image)
SparseColorImage.argtypes = [POINTER(Image), ChannelType, SparseColorMethod, size_t, POINTER(c_double), POINTER(ExceptionInfo)]

# values for enumeration 'AlignType'
AlignType = c_int # enum

# values for enumeration 'ClipPathUnits'
ClipPathUnits = c_int # enum

# values for enumeration 'DecorationType'
DecorationType = c_int # enum

# values for enumeration 'DirectionType'
DirectionType = c_int # enum

# values for enumeration 'FillRule'
FillRule = c_int # enum

# values for enumeration 'GradientType'
GradientType = c_int # enum

# values for enumeration 'LineCap'
LineCap = c_int # enum

# values for enumeration 'LineJoin'
LineJoin = c_int # enum

# values for enumeration 'PrimitiveType'
PrimitiveType = c_int # enum

# values for enumeration 'ReferenceType'
ReferenceType = c_int # enum

# values for enumeration 'SpreadMethod'
SpreadMethod = c_int # enum
class _PointInfo(Structure):
    pass
PointInfo = _PointInfo
class _StopInfo(Structure):
    pass
StopInfo = _StopInfo
class _GradientInfo(Structure):
    pass
GradientInfo = _GradientInfo
class _ElementReference(Structure):
    pass
ElementReference = _ElementReference
class _PrimitiveInfo(Structure):
    pass
PrimitiveInfo = _PrimitiveInfo
AcquireDrawInfo = _lib.AcquireDrawInfo
AcquireDrawInfo.restype = POINTER(DrawInfo)
AcquireDrawInfo.argtypes = []
CloneDrawInfo = _lib.CloneDrawInfo
CloneDrawInfo.restype = POINTER(DrawInfo)
CloneDrawInfo.argtypes = [POINTER(ImageInfo), POINTER(DrawInfo)]
DestroyDrawInfo = _lib.DestroyDrawInfo
DestroyDrawInfo.restype = POINTER(DrawInfo)
DestroyDrawInfo.argtypes = [POINTER(DrawInfo)]
DrawAffineImage = _lib.DrawAffineImage
DrawAffineImage.restype = MagickBooleanType
DrawAffineImage.argtypes = [POINTER(Image), POINTER(Image), POINTER(AffineMatrix)]
DrawClipPath = _lib.DrawClipPath
DrawClipPath.restype = MagickBooleanType
DrawClipPath.argtypes = [POINTER(Image), POINTER(DrawInfo), STRING]
DrawGradientImage = _lib.DrawGradientImage
DrawGradientImage.restype = MagickBooleanType
DrawGradientImage.argtypes = [POINTER(Image), POINTER(DrawInfo)]
DrawImage = _lib.DrawImage
DrawImage.restype = MagickBooleanType
DrawImage.argtypes = [POINTER(Image), POINTER(DrawInfo)]
DrawPatternPath = _lib.DrawPatternPath
DrawPatternPath.restype = MagickBooleanType
DrawPatternPath.argtypes = [POINTER(Image), POINTER(DrawInfo), STRING, POINTER(POINTER(Image))]
DrawPrimitive = _lib.DrawPrimitive
DrawPrimitive.restype = MagickBooleanType
DrawPrimitive.argtypes = [POINTER(Image), POINTER(DrawInfo), POINTER(PrimitiveInfo)]
GetAffineMatrix = _lib.GetAffineMatrix
GetAffineMatrix.restype = None
GetAffineMatrix.argtypes = [POINTER(AffineMatrix)]
GetDrawInfo = _lib.GetDrawInfo
GetDrawInfo.restype = None
GetDrawInfo.argtypes = [POINTER(ImageInfo), POINTER(DrawInfo)]

# values for enumeration 'PreviewType'
PreviewType = c_int # enum
AdaptiveBlurImage = _lib.AdaptiveBlurImage
AdaptiveBlurImage.restype = POINTER(Image)
AdaptiveBlurImage.argtypes = [POINTER(Image), c_double, c_double, POINTER(ExceptionInfo)]
AdaptiveBlurImageChannel = _lib.AdaptiveBlurImageChannel
AdaptiveBlurImageChannel.restype = POINTER(Image)
AdaptiveBlurImageChannel.argtypes = [POINTER(Image), ChannelType, c_double, c_double, POINTER(ExceptionInfo)]
AdaptiveSharpenImage = _lib.AdaptiveSharpenImage
AdaptiveSharpenImage.restype = POINTER(Image)
AdaptiveSharpenImage.argtypes = [POINTER(Image), c_double, c_double, POINTER(ExceptionInfo)]
AdaptiveSharpenImageChannel = _lib.AdaptiveSharpenImageChannel
AdaptiveSharpenImageChannel.restype = POINTER(Image)
AdaptiveSharpenImageChannel.argtypes = [POINTER(Image), ChannelType, c_double, c_double, POINTER(ExceptionInfo)]
BlurImage = _lib.BlurImage
BlurImage.restype = POINTER(Image)
BlurImage.argtypes = [POINTER(Image), c_double, c_double, POINTER(ExceptionInfo)]
BlurImageChannel = _lib.BlurImageChannel
BlurImageChannel.restype = POINTER(Image)
BlurImageChannel.argtypes = [POINTER(Image), ChannelType, c_double, c_double, POINTER(ExceptionInfo)]
ConvolveImage = _lib.ConvolveImage
ConvolveImage.restype = POINTER(Image)
ConvolveImage.argtypes = [POINTER(Image), size_t, POINTER(c_double), POINTER(ExceptionInfo)]
ConvolveImageChannel = _lib.ConvolveImageChannel
ConvolveImageChannel.restype = POINTER(Image)
ConvolveImageChannel.argtypes = [POINTER(Image), ChannelType, size_t, POINTER(c_double), POINTER(ExceptionInfo)]
DespeckleImage = _lib.DespeckleImage
DespeckleImage.restype = POINTER(Image)
DespeckleImage.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
EdgeImage = _lib.EdgeImage
EdgeImage.restype = POINTER(Image)
EdgeImage.argtypes = [POINTER(Image), c_double, POINTER(ExceptionInfo)]
EmbossImage = _lib.EmbossImage
EmbossImage.restype = POINTER(Image)
EmbossImage.argtypes = [POINTER(Image), c_double, c_double, POINTER(ExceptionInfo)]
FilterImage = _lib.FilterImage
FilterImage.restype = POINTER(Image)
FilterImage.argtypes = [POINTER(Image), POINTER(KernelInfo), POINTER(ExceptionInfo)]
FilterImageChannel = _lib.FilterImageChannel
FilterImageChannel.restype = POINTER(Image)
FilterImageChannel.argtypes = [POINTER(Image), ChannelType, POINTER(KernelInfo), POINTER(ExceptionInfo)]
GaussianBlurImage = _lib.GaussianBlurImage
GaussianBlurImage.restype = POINTER(Image)
GaussianBlurImage.argtypes = [POINTER(Image), c_double, c_double, POINTER(ExceptionInfo)]
GaussianBlurImageChannel = _lib.GaussianBlurImageChannel
GaussianBlurImageChannel.restype = POINTER(Image)
GaussianBlurImageChannel.argtypes = [POINTER(Image), ChannelType, c_double, c_double, POINTER(ExceptionInfo)]
MedianFilterImage = _lib.MedianFilterImage
MedianFilterImage.restype = POINTER(Image)
MedianFilterImage.argtypes = [POINTER(Image), c_double, POINTER(ExceptionInfo)]
MotionBlurImage = _lib.MotionBlurImage
MotionBlurImage.restype = POINTER(Image)
MotionBlurImage.argtypes = [POINTER(Image), c_double, c_double, c_double, POINTER(ExceptionInfo)]
MotionBlurImageChannel = _lib.MotionBlurImageChannel
MotionBlurImageChannel.restype = POINTER(Image)
MotionBlurImageChannel.argtypes = [POINTER(Image), ChannelType, c_double, c_double, c_double, POINTER(ExceptionInfo)]
PreviewImage = _lib.PreviewImage
PreviewImage.restype = POINTER(Image)
PreviewImage.argtypes = [POINTER(Image), PreviewType, POINTER(ExceptionInfo)]
RadialBlurImage = _lib.RadialBlurImage
RadialBlurImage.restype = POINTER(Image)
RadialBlurImage.argtypes = [POINTER(Image), c_double, POINTER(ExceptionInfo)]
RadialBlurImageChannel = _lib.RadialBlurImageChannel
RadialBlurImageChannel.restype = POINTER(Image)
RadialBlurImageChannel.argtypes = [POINTER(Image), ChannelType, c_double, POINTER(ExceptionInfo)]
ReduceNoiseImage = _lib.ReduceNoiseImage
ReduceNoiseImage.restype = POINTER(Image)
ReduceNoiseImage.argtypes = [POINTER(Image), c_double, POINTER(ExceptionInfo)]
SelectiveBlurImage = _lib.SelectiveBlurImage
SelectiveBlurImage.restype = POINTER(Image)
SelectiveBlurImage.argtypes = [POINTER(Image), c_double, c_double, c_double, POINTER(ExceptionInfo)]
SelectiveBlurImageChannel = _lib.SelectiveBlurImageChannel
SelectiveBlurImageChannel.restype = POINTER(Image)
SelectiveBlurImageChannel.argtypes = [POINTER(Image), ChannelType, c_double, c_double, c_double, POINTER(ExceptionInfo)]
ShadeImage = _lib.ShadeImage
ShadeImage.restype = POINTER(Image)
ShadeImage.argtypes = [POINTER(Image), MagickBooleanType, c_double, c_double, POINTER(ExceptionInfo)]
SharpenImage = _lib.SharpenImage
SharpenImage.restype = POINTER(Image)
SharpenImage.argtypes = [POINTER(Image), c_double, c_double, POINTER(ExceptionInfo)]
SharpenImageChannel = _lib.SharpenImageChannel
SharpenImageChannel.restype = POINTER(Image)
SharpenImageChannel.argtypes = [POINTER(Image), ChannelType, c_double, c_double, POINTER(ExceptionInfo)]
SpreadImage = _lib.SpreadImage
SpreadImage.restype = POINTER(Image)
SpreadImage.argtypes = [POINTER(Image), c_double, POINTER(ExceptionInfo)]
UnsharpMaskImage = _lib.UnsharpMaskImage
UnsharpMaskImage.restype = POINTER(Image)
UnsharpMaskImage.argtypes = [POINTER(Image), c_double, c_double, c_double, c_double, POINTER(ExceptionInfo)]
UnsharpMaskImageChannel = _lib.UnsharpMaskImageChannel
UnsharpMaskImageChannel.restype = POINTER(Image)
UnsharpMaskImageChannel.argtypes = [POINTER(Image), ChannelType, c_double, c_double, c_double, c_double, POINTER(ExceptionInfo)]
AutoGammaImage = _lib.AutoGammaImage
AutoGammaImage.restype = MagickBooleanType
AutoGammaImage.argtypes = [POINTER(Image)]
AutoGammaImageChannel = _lib.AutoGammaImageChannel
AutoGammaImageChannel.restype = MagickBooleanType
AutoGammaImageChannel.argtypes = [POINTER(Image), ChannelType]
AutoLevelImage = _lib.AutoLevelImage
AutoLevelImage.restype = MagickBooleanType
AutoLevelImage.argtypes = [POINTER(Image)]
AutoLevelImageChannel = _lib.AutoLevelImageChannel
AutoLevelImageChannel.restype = MagickBooleanType
AutoLevelImageChannel.argtypes = [POINTER(Image), ChannelType]
BrightnessContrastImage = _lib.BrightnessContrastImage
BrightnessContrastImage.restype = MagickBooleanType
BrightnessContrastImage.argtypes = [POINTER(Image), c_double, c_double]
BrightnessContrastImageChannel = _lib.BrightnessContrastImageChannel
BrightnessContrastImageChannel.restype = MagickBooleanType
BrightnessContrastImageChannel.argtypes = [POINTER(Image), ChannelType, c_double, c_double]
ClutImage = _lib.ClutImage
ClutImage.restype = MagickBooleanType
ClutImage.argtypes = [POINTER(Image), POINTER(Image)]
ClutImageChannel = _lib.ClutImageChannel
ClutImageChannel.restype = MagickBooleanType
ClutImageChannel.argtypes = [POINTER(Image), ChannelType, POINTER(Image)]
ColorDecisionListImage = _lib.ColorDecisionListImage
ColorDecisionListImage.restype = MagickBooleanType
ColorDecisionListImage.argtypes = [POINTER(Image), STRING]
ContrastImage = _lib.ContrastImage
ContrastImage.restype = MagickBooleanType
ContrastImage.argtypes = [POINTER(Image), MagickBooleanType]
ContrastStretchImage = _lib.ContrastStretchImage
ContrastStretchImage.restype = MagickBooleanType
ContrastStretchImage.argtypes = [POINTER(Image), STRING]
ContrastStretchImageChannel = _lib.ContrastStretchImageChannel
ContrastStretchImageChannel.restype = MagickBooleanType
ContrastStretchImageChannel.argtypes = [POINTER(Image), ChannelType, c_double, c_double]
EqualizeImage = _lib.EqualizeImage
EqualizeImage.restype = MagickBooleanType
EqualizeImage.argtypes = [POINTER(Image)]
EqualizeImageChannel = _lib.EqualizeImageChannel
EqualizeImageChannel.restype = MagickBooleanType
EqualizeImageChannel.argtypes = [POINTER(Image), ChannelType]
GammaImage = _lib.GammaImage
GammaImage.restype = MagickBooleanType
GammaImage.argtypes = [POINTER(Image), STRING]
GammaImageChannel = _lib.GammaImageChannel
GammaImageChannel.restype = MagickBooleanType
GammaImageChannel.argtypes = [POINTER(Image), ChannelType, c_double]
HaldClutImage = _lib.HaldClutImage
HaldClutImage.restype = MagickBooleanType
HaldClutImage.argtypes = [POINTER(Image), POINTER(Image)]
HaldClutImageChannel = _lib.HaldClutImageChannel
HaldClutImageChannel.restype = MagickBooleanType
HaldClutImageChannel.argtypes = [POINTER(Image), ChannelType, POINTER(Image)]
LevelImage = _lib.LevelImage
LevelImage.restype = MagickBooleanType
LevelImage.argtypes = [POINTER(Image), STRING]
LevelImageChannel = _lib.LevelImageChannel
LevelImageChannel.restype = MagickBooleanType
LevelImageChannel.argtypes = [POINTER(Image), ChannelType, c_double, c_double, c_double]
LevelizeImage = _lib.LevelizeImage
LevelizeImage.restype = MagickBooleanType
LevelizeImage.argtypes = [POINTER(Image), c_double, c_double, c_double]
LevelizeImageChannel = _lib.LevelizeImageChannel
LevelizeImageChannel.restype = MagickBooleanType
LevelizeImageChannel.argtypes = [POINTER(Image), ChannelType, c_double, c_double, c_double]
LevelColorsImage = _lib.LevelColorsImage
LevelColorsImage.restype = MagickBooleanType
LevelColorsImage.argtypes = [POINTER(Image), POINTER(MagickPixelPacket), POINTER(MagickPixelPacket), MagickBooleanType]
LevelColorsImageChannel = _lib.LevelColorsImageChannel
LevelColorsImageChannel.restype = MagickBooleanType
LevelColorsImageChannel.argtypes = [POINTER(Image), ChannelType, POINTER(MagickPixelPacket), POINTER(MagickPixelPacket), MagickBooleanType]
LinearStretchImage = _lib.LinearStretchImage
LinearStretchImage.restype = MagickBooleanType
LinearStretchImage.argtypes = [POINTER(Image), c_double, c_double]
ModulateImage = _lib.ModulateImage
ModulateImage.restype = MagickBooleanType
ModulateImage.argtypes = [POINTER(Image), STRING]
NegateImage = _lib.NegateImage
NegateImage.restype = MagickBooleanType
NegateImage.argtypes = [POINTER(Image), MagickBooleanType]
NegateImageChannel = _lib.NegateImageChannel
NegateImageChannel.restype = MagickBooleanType
NegateImageChannel.argtypes = [POINTER(Image), ChannelType, MagickBooleanType]
NormalizeImage = _lib.NormalizeImage
NormalizeImage.restype = MagickBooleanType
NormalizeImage.argtypes = [POINTER(Image)]
NormalizeImageChannel = _lib.NormalizeImageChannel
NormalizeImageChannel.restype = MagickBooleanType
NormalizeImageChannel.argtypes = [POINTER(Image), ChannelType]
SigmoidalContrastImage = _lib.SigmoidalContrastImage
SigmoidalContrastImage.restype = MagickBooleanType
SigmoidalContrastImage.argtypes = [POINTER(Image), MagickBooleanType, STRING]
SigmoidalContrastImageChannel = _lib.SigmoidalContrastImageChannel
SigmoidalContrastImageChannel.restype = MagickBooleanType
SigmoidalContrastImageChannel.argtypes = [POINTER(Image), ChannelType, MagickBooleanType, c_double, c_double]
EnhanceImage = _lib.EnhanceImage
EnhanceImage.restype = POINTER(Image)
EnhanceImage.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
ErrorHandler = CFUNCTYPE(None, ExceptionType, STRING, STRING)
FatalErrorHandler = CFUNCTYPE(None, ExceptionType, STRING, STRING)
WarningHandler = CFUNCTYPE(None, ExceptionType, STRING, STRING)
GetExceptionMessage = _lib.GetExceptionMessage
GetExceptionMessage.restype = STRING
GetExceptionMessage.argtypes = [c_int]
GetLocaleExceptionMessage = _lib.GetLocaleExceptionMessage
GetLocaleExceptionMessage.restype = STRING
GetLocaleExceptionMessage.argtypes = [ExceptionType, STRING]
SetErrorHandler = _lib.SetErrorHandler
SetErrorHandler.restype = ErrorHandler
SetErrorHandler.argtypes = [ErrorHandler]
AcquireExceptionInfo = _lib.AcquireExceptionInfo
AcquireExceptionInfo.restype = POINTER(ExceptionInfo)
AcquireExceptionInfo.argtypes = []
DestroyExceptionInfo = _lib.DestroyExceptionInfo
DestroyExceptionInfo.restype = POINTER(ExceptionInfo)
DestroyExceptionInfo.argtypes = [POINTER(ExceptionInfo)]
SetFatalErrorHandler = _lib.SetFatalErrorHandler
SetFatalErrorHandler.restype = FatalErrorHandler
SetFatalErrorHandler.argtypes = [FatalErrorHandler]
ThrowException = _lib.ThrowException
ThrowException.restype = MagickBooleanType
ThrowException.argtypes = [POINTER(ExceptionInfo), ExceptionType, STRING, STRING]
ThrowMagickException = _lib.ThrowMagickException
ThrowMagickException.restype = MagickBooleanType
ThrowMagickException.argtypes = [POINTER(ExceptionInfo), STRING, STRING, size_t, ExceptionType, STRING, STRING]
ThrowMagickExceptionList = _lib.ThrowMagickExceptionList
ThrowMagickExceptionList.restype = MagickBooleanType
ThrowMagickExceptionList.argtypes = [POINTER(ExceptionInfo), STRING, STRING, size_t, ExceptionType, STRING, STRING, POINTER(__va_list_tag)]
CatchException = _lib.CatchException
CatchException.restype = None
CatchException.argtypes = [POINTER(ExceptionInfo)]
ClearMagickException = _lib.ClearMagickException
ClearMagickException.restype = None
ClearMagickException.argtypes = [POINTER(ExceptionInfo)]
GetExceptionInfo = _lib.GetExceptionInfo
GetExceptionInfo.restype = None
GetExceptionInfo.argtypes = [POINTER(ExceptionInfo)]
InheritException = _lib.InheritException
InheritException.restype = None
InheritException.argtypes = [POINTER(ExceptionInfo), POINTER(ExceptionInfo)]
MagickError = _lib.MagickError
MagickError.restype = None
MagickError.argtypes = [ExceptionType, STRING, STRING]
MagickFatalError = _lib.MagickFatalError
MagickFatalError.restype = None
MagickFatalError.argtypes = [ExceptionType, STRING, STRING]
MagickWarning = _lib.MagickWarning
MagickWarning.restype = None
MagickWarning.argtypes = [ExceptionType, STRING, STRING]
SetWarningHandler = _lib.SetWarningHandler
SetWarningHandler.restype = WarningHandler
SetWarningHandler.argtypes = [WarningHandler]
class _ChannelFeatures(Structure):
    pass
ChannelFeatures = _ChannelFeatures
GetImageChannelFeatures = _lib.GetImageChannelFeatures
GetImageChannelFeatures.restype = POINTER(ChannelFeatures)
GetImageChannelFeatures.argtypes = [POINTER(Image), size_t, POINTER(ExceptionInfo)]
ForwardFourierTransformImage = _lib.ForwardFourierTransformImage
ForwardFourierTransformImage.restype = POINTER(Image)
ForwardFourierTransformImage.argtypes = [POINTER(Image), MagickBooleanType, POINTER(ExceptionInfo)]
InverseFourierTransformImage = _lib.InverseFourierTransformImage
InverseFourierTransformImage.restype = POINTER(Image)
InverseFourierTransformImage.argtypes = [POINTER(Image), POINTER(Image), MagickBooleanType, POINTER(ExceptionInfo)]

# values for enumeration 'NoiseType'
NoiseType = c_int # enum
AddNoiseImage = _lib.AddNoiseImage
AddNoiseImage.restype = POINTER(Image)
AddNoiseImage.argtypes = [POINTER(Image), NoiseType, POINTER(ExceptionInfo)]
AddNoiseImageChannel = _lib.AddNoiseImageChannel
AddNoiseImageChannel.restype = POINTER(Image)
AddNoiseImageChannel.argtypes = [POINTER(Image), ChannelType, NoiseType, POINTER(ExceptionInfo)]
BlueShiftImage = _lib.BlueShiftImage
BlueShiftImage.restype = POINTER(Image)
BlueShiftImage.argtypes = [POINTER(Image), c_double, POINTER(ExceptionInfo)]
CharcoalImage = _lib.CharcoalImage
CharcoalImage.restype = POINTER(Image)
CharcoalImage.argtypes = [POINTER(Image), c_double, c_double, POINTER(ExceptionInfo)]
ColorizeImage = _lib.ColorizeImage
ColorizeImage.restype = POINTER(Image)
ColorizeImage.argtypes = [POINTER(Image), STRING, PixelPacket, POINTER(ExceptionInfo)]
ColorMatrixImage = _lib.ColorMatrixImage
ColorMatrixImage.restype = POINTER(Image)
ColorMatrixImage.argtypes = [POINTER(Image), POINTER(KernelInfo), POINTER(ExceptionInfo)]
FxImage = _lib.FxImage
FxImage.restype = POINTER(Image)
FxImage.argtypes = [POINTER(Image), STRING, POINTER(ExceptionInfo)]
FxImageChannel = _lib.FxImageChannel
FxImageChannel.restype = POINTER(Image)
FxImageChannel.argtypes = [POINTER(Image), ChannelType, STRING, POINTER(ExceptionInfo)]
ImplodeImage = _lib.ImplodeImage
ImplodeImage.restype = POINTER(Image)
ImplodeImage.argtypes = [POINTER(Image), c_double, POINTER(ExceptionInfo)]
MorphImages = _lib.MorphImages
MorphImages.restype = POINTER(Image)
MorphImages.argtypes = [POINTER(Image), size_t, POINTER(ExceptionInfo)]
PolaroidImage = _lib.PolaroidImage
PolaroidImage.restype = POINTER(Image)
PolaroidImage.argtypes = [POINTER(Image), POINTER(DrawInfo), c_double, POINTER(ExceptionInfo)]
SepiaToneImage = _lib.SepiaToneImage
SepiaToneImage.restype = POINTER(Image)
SepiaToneImage.argtypes = [POINTER(Image), c_double, POINTER(ExceptionInfo)]
ShadowImage = _lib.ShadowImage
ShadowImage.restype = POINTER(Image)
ShadowImage.argtypes = [POINTER(Image), c_double, c_double, ssize_t, ssize_t, POINTER(ExceptionInfo)]
SketchImage = _lib.SketchImage
SketchImage.restype = POINTER(Image)
SketchImage.argtypes = [POINTER(Image), c_double, c_double, c_double, POINTER(ExceptionInfo)]
SteganoImage = _lib.SteganoImage
SteganoImage.restype = POINTER(Image)
SteganoImage.argtypes = [POINTER(Image), POINTER(Image), POINTER(ExceptionInfo)]
StereoImage = _lib.StereoImage
StereoImage.restype = POINTER(Image)
StereoImage.argtypes = [POINTER(Image), POINTER(Image), POINTER(ExceptionInfo)]
StereoAnaglyphImage = _lib.StereoAnaglyphImage
StereoAnaglyphImage.restype = POINTER(Image)
StereoAnaglyphImage.argtypes = [POINTER(Image), POINTER(Image), ssize_t, ssize_t, POINTER(ExceptionInfo)]
SwirlImage = _lib.SwirlImage
SwirlImage.restype = POINTER(Image)
SwirlImage.argtypes = [POINTER(Image), c_double, POINTER(ExceptionInfo)]
TintImage = _lib.TintImage
TintImage.restype = POINTER(Image)
TintImage.argtypes = [POINTER(Image), STRING, PixelPacket, POINTER(ExceptionInfo)]
VignetteImage = _lib.VignetteImage
VignetteImage.restype = POINTER(Image)
VignetteImage.argtypes = [POINTER(Image), c_double, c_double, ssize_t, ssize_t, POINTER(ExceptionInfo)]
WaveImage = _lib.WaveImage
WaveImage.restype = POINTER(Image)
WaveImage.argtypes = [POINTER(Image), c_double, c_double, POINTER(ExceptionInfo)]
class _SegmentInfo(Structure):
    pass
SegmentInfo = _SegmentInfo
PlasmaImage = _lib.PlasmaImage
PlasmaImage.restype = MagickBooleanType
PlasmaImage.argtypes = [POINTER(Image), POINTER(SegmentInfo), size_t, size_t]
SolarizeImage = _lib.SolarizeImage
SolarizeImage.restype = MagickBooleanType
SolarizeImage.argtypes = [POINTER(Image), c_double]
ExpandAffine = _lib.ExpandAffine
ExpandAffine.restype = c_double
ExpandAffine.argtypes = [POINTER(AffineMatrix)]
class _RandomInfo(Structure):
    pass
RandomInfo = _RandomInfo
GenerateDifferentialNoise = _lib.GenerateDifferentialNoise
GenerateDifferentialNoise.restype = c_double
GenerateDifferentialNoise.argtypes = [POINTER(RandomInfo), Quantum, NoiseType, MagickRealType]
GetOptimalKernelWidth = _lib.GetOptimalKernelWidth
GetOptimalKernelWidth.restype = size_t
GetOptimalKernelWidth.argtypes = [c_double, c_double]
GetOptimalKernelWidth1D = _lib.GetOptimalKernelWidth1D
GetOptimalKernelWidth1D.restype = size_t
GetOptimalKernelWidth1D.argtypes = [c_double, c_double]
GetOptimalKernelWidth2D = _lib.GetOptimalKernelWidth2D
GetOptimalKernelWidth2D.restype = size_t
GetOptimalKernelWidth2D.argtypes = [c_double, c_double]
ConvertHSBToRGB = _lib.ConvertHSBToRGB
ConvertHSBToRGB.restype = None
ConvertHSBToRGB.argtypes = [c_double, c_double, c_double, POINTER(Quantum), POINTER(Quantum), POINTER(Quantum)]
ConvertHSLToRGB = _lib.ConvertHSLToRGB
ConvertHSLToRGB.restype = None
ConvertHSLToRGB.argtypes = [c_double, c_double, c_double, POINTER(Quantum), POINTER(Quantum), POINTER(Quantum)]
ConvertHWBToRGB = _lib.ConvertHWBToRGB
ConvertHWBToRGB.restype = None
ConvertHWBToRGB.argtypes = [c_double, c_double, c_double, POINTER(Quantum), POINTER(Quantum), POINTER(Quantum)]
ConvertRGBToHSB = _lib.ConvertRGBToHSB
ConvertRGBToHSB.restype = None
ConvertRGBToHSB.argtypes = [Quantum, Quantum, Quantum, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
ConvertRGBToHSL = _lib.ConvertRGBToHSL
ConvertRGBToHSL.restype = None
ConvertRGBToHSL.argtypes = [Quantum, Quantum, Quantum, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
ConvertRGBToHWB = _lib.ConvertRGBToHWB
ConvertRGBToHWB.restype = None
ConvertRGBToHWB.argtypes = [Quantum, Quantum, Quantum, POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# values for enumeration 'GeometryFlags'
GeometryFlags = c_int # enum

# values for enumeration 'GravityType'
GravityType = c_int # enum
class _GeometryInfo(Structure):
    pass
GeometryInfo = _GeometryInfo
class _OffsetInfo(Structure):
    pass
OffsetInfo = _OffsetInfo
GetPageGeometry = _lib.GetPageGeometry
GetPageGeometry.restype = STRING
GetPageGeometry.argtypes = [STRING]
IsGeometry = _lib.IsGeometry
IsGeometry.restype = MagickBooleanType
IsGeometry.argtypes = [STRING]
IsSceneGeometry = _lib.IsSceneGeometry
IsSceneGeometry.restype = MagickBooleanType
IsSceneGeometry.argtypes = [STRING, MagickBooleanType]
GetGeometry = _lib.GetGeometry
GetGeometry.restype = MagickStatusType
GetGeometry.argtypes = [STRING, POINTER(ssize_t), POINTER(ssize_t), POINTER(size_t), POINTER(size_t)]
ParseAbsoluteGeometry = _lib.ParseAbsoluteGeometry
ParseAbsoluteGeometry.restype = MagickStatusType
ParseAbsoluteGeometry.argtypes = [STRING, POINTER(RectangleInfo)]
ParseAffineGeometry = _lib.ParseAffineGeometry
ParseAffineGeometry.restype = MagickStatusType
ParseAffineGeometry.argtypes = [STRING, POINTER(AffineMatrix), POINTER(ExceptionInfo)]
ParseGeometry = _lib.ParseGeometry
ParseGeometry.restype = MagickStatusType
ParseGeometry.argtypes = [STRING, POINTER(GeometryInfo)]
ParseGravityGeometry = _lib.ParseGravityGeometry
ParseGravityGeometry.restype = MagickStatusType
ParseGravityGeometry.argtypes = [POINTER(Image), STRING, POINTER(RectangleInfo), POINTER(ExceptionInfo)]
ParseMetaGeometry = _lib.ParseMetaGeometry
ParseMetaGeometry.restype = MagickStatusType
ParseMetaGeometry.argtypes = [STRING, POINTER(ssize_t), POINTER(ssize_t), POINTER(size_t), POINTER(size_t)]
ParsePageGeometry = _lib.ParsePageGeometry
ParsePageGeometry.restype = MagickStatusType
ParsePageGeometry.argtypes = [POINTER(Image), STRING, POINTER(RectangleInfo), POINTER(ExceptionInfo)]
ParseRegionGeometry = _lib.ParseRegionGeometry
ParseRegionGeometry.restype = MagickStatusType
ParseRegionGeometry.argtypes = [POINTER(Image), STRING, POINTER(RectangleInfo), POINTER(ExceptionInfo)]
GravityAdjustGeometry = _lib.GravityAdjustGeometry
GravityAdjustGeometry.restype = None
GravityAdjustGeometry.argtypes = [size_t, size_t, GravityType, POINTER(RectangleInfo)]
SetGeometry = _lib.SetGeometry
SetGeometry.restype = None
SetGeometry.argtypes = [POINTER(Image), POINTER(RectangleInfo)]
SetGeometryInfo = _lib.SetGeometryInfo
SetGeometryInfo.restype = None
SetGeometryInfo.argtypes = [POINTER(GeometryInfo)]
class _HashmapInfo(Structure):
    pass
HashmapInfo = _HashmapInfo
DestroyHashmap = _lib.DestroyHashmap
DestroyHashmap.restype = POINTER(HashmapInfo)
DestroyHashmap.argtypes = [POINTER(HashmapInfo)]
NewHashmap = _lib.NewHashmap
NewHashmap.restype = POINTER(HashmapInfo)
NewHashmap.argtypes = [size_t, CFUNCTYPE(size_t, c_void_p), CFUNCTYPE(MagickBooleanType, c_void_p, c_void_p), CFUNCTYPE(c_void_p, c_void_p), CFUNCTYPE(c_void_p, c_void_p)]
DestroyLinkedList = _lib.DestroyLinkedList
DestroyLinkedList.restype = POINTER(LinkedListInfo)
DestroyLinkedList.argtypes = [POINTER(LinkedListInfo), CFUNCTYPE(c_void_p, c_void_p)]
NewLinkedList = _lib.NewLinkedList
NewLinkedList.restype = POINTER(LinkedListInfo)
NewLinkedList.argtypes = [size_t]
AppendValueToLinkedList = _lib.AppendValueToLinkedList
AppendValueToLinkedList.restype = MagickBooleanType
AppendValueToLinkedList.argtypes = [POINTER(LinkedListInfo), c_void_p]
CompareHashmapString = _lib.CompareHashmapString
CompareHashmapString.restype = MagickBooleanType
CompareHashmapString.argtypes = [c_void_p, c_void_p]
CompareHashmapStringInfo = _lib.CompareHashmapStringInfo
CompareHashmapStringInfo.restype = MagickBooleanType
CompareHashmapStringInfo.argtypes = [c_void_p, c_void_p]
InsertValueInLinkedList = _lib.InsertValueInLinkedList
InsertValueInLinkedList.restype = MagickBooleanType
InsertValueInLinkedList.argtypes = [POINTER(LinkedListInfo), size_t, c_void_p]
InsertValueInSortedLinkedList = _lib.InsertValueInSortedLinkedList
InsertValueInSortedLinkedList.restype = MagickBooleanType
InsertValueInSortedLinkedList.argtypes = [POINTER(LinkedListInfo), CFUNCTYPE(c_int, c_void_p, c_void_p), POINTER(c_void_p), c_void_p]
IsHashmapEmpty = _lib.IsHashmapEmpty
IsHashmapEmpty.restype = MagickBooleanType
IsHashmapEmpty.argtypes = [POINTER(HashmapInfo)]
IsLinkedListEmpty = _lib.IsLinkedListEmpty
IsLinkedListEmpty.restype = MagickBooleanType
IsLinkedListEmpty.argtypes = [POINTER(LinkedListInfo)]
LinkedListToArray = _lib.LinkedListToArray
LinkedListToArray.restype = MagickBooleanType
LinkedListToArray.argtypes = [POINTER(LinkedListInfo), POINTER(c_void_p)]
PutEntryInHashmap = _lib.PutEntryInHashmap
PutEntryInHashmap.restype = MagickBooleanType
PutEntryInHashmap.argtypes = [POINTER(HashmapInfo), c_void_p, c_void_p]
GetNumberOfElementsInLinkedList = _lib.GetNumberOfElementsInLinkedList
GetNumberOfElementsInLinkedList.restype = size_t
GetNumberOfElementsInLinkedList.argtypes = [POINTER(LinkedListInfo)]
GetNumberOfEntriesInHashmap = _lib.GetNumberOfEntriesInHashmap
GetNumberOfEntriesInHashmap.restype = size_t
GetNumberOfEntriesInHashmap.argtypes = [POINTER(HashmapInfo)]
HashPointerType = _lib.HashPointerType
HashPointerType.restype = size_t
HashPointerType.argtypes = [c_void_p]
HashStringType = _lib.HashStringType
HashStringType.restype = size_t
HashStringType.argtypes = [c_void_p]
HashStringInfoType = _lib.HashStringInfoType
HashStringInfoType.restype = size_t
HashStringInfoType.argtypes = [c_void_p]
ClearLinkedList = _lib.ClearLinkedList
ClearLinkedList.restype = None
ClearLinkedList.argtypes = [POINTER(LinkedListInfo), CFUNCTYPE(c_void_p, c_void_p)]
GetLastValueInLinkedList = _lib.GetLastValueInLinkedList
GetLastValueInLinkedList.restype = c_void_p
GetLastValueInLinkedList.argtypes = [POINTER(LinkedListInfo)]
GetNextKeyInHashmap = _lib.GetNextKeyInHashmap
GetNextKeyInHashmap.restype = c_void_p
GetNextKeyInHashmap.argtypes = [POINTER(HashmapInfo)]
GetNextValueInHashmap = _lib.GetNextValueInHashmap
GetNextValueInHashmap.restype = c_void_p
GetNextValueInHashmap.argtypes = [POINTER(HashmapInfo)]
GetNextValueInLinkedList = _lib.GetNextValueInLinkedList
GetNextValueInLinkedList.restype = c_void_p
GetNextValueInLinkedList.argtypes = [POINTER(LinkedListInfo)]
GetValueFromHashmap = _lib.GetValueFromHashmap
GetValueFromHashmap.restype = c_void_p
GetValueFromHashmap.argtypes = [POINTER(HashmapInfo), c_void_p]
GetValueFromLinkedList = _lib.GetValueFromLinkedList
GetValueFromLinkedList.restype = c_void_p
GetValueFromLinkedList.argtypes = [POINTER(LinkedListInfo), size_t]
RemoveElementByValueFromLinkedList = _lib.RemoveElementByValueFromLinkedList
RemoveElementByValueFromLinkedList.restype = c_void_p
RemoveElementByValueFromLinkedList.argtypes = [POINTER(LinkedListInfo), c_void_p]
RemoveElementFromLinkedList = _lib.RemoveElementFromLinkedList
RemoveElementFromLinkedList.restype = c_void_p
RemoveElementFromLinkedList.argtypes = [POINTER(LinkedListInfo), size_t]
RemoveEntryFromHashmap = _lib.RemoveEntryFromHashmap
RemoveEntryFromHashmap.restype = c_void_p
RemoveEntryFromHashmap.argtypes = [POINTER(HashmapInfo), c_void_p]
RemoveLastElementFromLinkedList = _lib.RemoveLastElementFromLinkedList
RemoveLastElementFromLinkedList.restype = c_void_p
RemoveLastElementFromLinkedList.argtypes = [POINTER(LinkedListInfo)]
ResetHashmapIterator = _lib.ResetHashmapIterator
ResetHashmapIterator.restype = None
ResetHashmapIterator.argtypes = [POINTER(HashmapInfo)]
ResetLinkedListIterator = _lib.ResetLinkedListIterator
ResetLinkedListIterator.restype = None
ResetLinkedListIterator.argtypes = [POINTER(LinkedListInfo)]
class _ColorPacket(Structure):
    pass
ColorPacket = _ColorPacket
GetImageHistogram = _lib.GetImageHistogram
GetImageHistogram.restype = POINTER(ColorPacket)
GetImageHistogram.argtypes = [POINTER(Image), POINTER(size_t), POINTER(ExceptionInfo)]
UniqueImageColors = _lib.UniqueImageColors
UniqueImageColors.restype = POINTER(Image)
UniqueImageColors.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
IsHistogramImage = _lib.IsHistogramImage
IsHistogramImage.restype = MagickBooleanType
IsHistogramImage.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
IsPaletteImage = _lib.IsPaletteImage
IsPaletteImage.restype = MagickBooleanType
IsPaletteImage.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
MinMaxStretchImage = _lib.MinMaxStretchImage
MinMaxStretchImage.restype = MagickBooleanType
MinMaxStretchImage.argtypes = [POINTER(Image), ChannelType, c_double, c_double]
GetNumberColors = _lib.GetNumberColors
GetNumberColors.restype = size_t
GetNumberColors.argtypes = [POINTER(Image), POINTER(FILE), POINTER(ExceptionInfo)]
IdentifyImage = _lib.IdentifyImage
IdentifyImage.restype = MagickBooleanType
IdentifyImage.argtypes = [POINTER(Image), POINTER(FILE), MagickBooleanType]

# values for enumeration 'AlphaChannelType'
AlphaChannelType = c_int # enum

# values for enumeration 'InterlaceType'
InterlaceType = c_int # enum

# values for enumeration 'OrientationType'
OrientationType = c_int # enum

# values for enumeration 'ResolutionType'
ResolutionType = c_int # enum
class _PrimaryInfo(Structure):
    pass
PrimaryInfo = _PrimaryInfo

# values for enumeration 'TransmitType'
TransmitType = c_int # enum
class _ChromaticityInfo(Structure):
    pass
ChromaticityInfo = _ChromaticityInfo
CatchImageException = _lib.CatchImageException
CatchImageException.restype = ExceptionType
CatchImageException.argtypes = [POINTER(Image)]
GetImageInfoFile = _lib.GetImageInfoFile
GetImageInfoFile.restype = POINTER(FILE)
GetImageInfoFile.argtypes = [POINTER(ImageInfo)]
AcquireImage = _lib.AcquireImage
AcquireImage.restype = POINTER(Image)
AcquireImage.argtypes = [POINTER(ImageInfo)]
AppendImages = _lib.AppendImages
AppendImages.restype = POINTER(Image)
AppendImages.argtypes = [POINTER(Image), MagickBooleanType, POINTER(ExceptionInfo)]
CloneImage = _lib.CloneImage
CloneImage.restype = POINTER(Image)
CloneImage.argtypes = [POINTER(Image), size_t, size_t, MagickBooleanType, POINTER(ExceptionInfo)]
CombineImages = _lib.CombineImages
CombineImages.restype = POINTER(Image)
CombineImages.argtypes = [POINTER(Image), ChannelType, POINTER(ExceptionInfo)]
DestroyImage = _lib.DestroyImage
DestroyImage.restype = POINTER(Image)
DestroyImage.argtypes = [POINTER(Image)]
GetImageClipMask = _lib.GetImageClipMask
GetImageClipMask.restype = POINTER(Image)
GetImageClipMask.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
GetImageMask = _lib.GetImageMask
GetImageMask.restype = POINTER(Image)
GetImageMask.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
NewMagickImage = _lib.NewMagickImage
NewMagickImage.restype = POINTER(Image)
NewMagickImage.argtypes = [POINTER(ImageInfo), size_t, size_t, POINTER(MagickPixelPacket)]
ReferenceImage = _lib.ReferenceImage
ReferenceImage.restype = POINTER(Image)
ReferenceImage.argtypes = [POINTER(Image)]
SeparateImages = _lib.SeparateImages
SeparateImages.restype = POINTER(Image)
SeparateImages.argtypes = [POINTER(Image), ChannelType, POINTER(ExceptionInfo)]
AcquireImageInfo = _lib.AcquireImageInfo
AcquireImageInfo.restype = POINTER(ImageInfo)
AcquireImageInfo.argtypes = []
CloneImageInfo = _lib.CloneImageInfo
CloneImageInfo.restype = POINTER(ImageInfo)
CloneImageInfo.argtypes = [POINTER(ImageInfo)]
DestroyImageInfo = _lib.DestroyImageInfo
DestroyImageInfo.restype = POINTER(ImageInfo)
DestroyImageInfo.argtypes = [POINTER(ImageInfo)]
ClipImage = _lib.ClipImage
ClipImage.restype = MagickBooleanType
ClipImage.argtypes = [POINTER(Image)]
ClipImagePath = _lib.ClipImagePath
ClipImagePath.restype = MagickBooleanType
ClipImagePath.argtypes = [POINTER(Image), STRING, MagickBooleanType]
GetImageAlphaChannel = _lib.GetImageAlphaChannel
GetImageAlphaChannel.restype = MagickBooleanType
GetImageAlphaChannel.argtypes = [POINTER(Image)]
IsTaintImage = _lib.IsTaintImage
IsTaintImage.restype = MagickBooleanType
IsTaintImage.argtypes = [POINTER(Image)]
IsMagickConflict = _lib.IsMagickConflict
IsMagickConflict.restype = MagickBooleanType
IsMagickConflict.argtypes = [STRING]
IsHighDynamicRangeImage = _lib.IsHighDynamicRangeImage
IsHighDynamicRangeImage.restype = MagickBooleanType
IsHighDynamicRangeImage.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
IsImageObject = _lib.IsImageObject
IsImageObject.restype = MagickBooleanType
IsImageObject.argtypes = [POINTER(Image)]
ListMagickInfo = _lib.ListMagickInfo
ListMagickInfo.restype = MagickBooleanType
ListMagickInfo.argtypes = [POINTER(FILE), POINTER(ExceptionInfo)]
ModifyImage = _lib.ModifyImage
ModifyImage.restype = MagickBooleanType
ModifyImage.argtypes = [POINTER(POINTER(Image)), POINTER(ExceptionInfo)]
ResetImagePage = _lib.ResetImagePage
ResetImagePage.restype = MagickBooleanType
ResetImagePage.argtypes = [POINTER(Image), STRING]
SeparateImageChannel = _lib.SeparateImageChannel
SeparateImageChannel.restype = MagickBooleanType
SeparateImageChannel.argtypes = [POINTER(Image), ChannelType]
SetImageAlphaChannel = _lib.SetImageAlphaChannel
SetImageAlphaChannel.restype = MagickBooleanType
SetImageAlphaChannel.argtypes = [POINTER(Image), AlphaChannelType]
SetImageBackgroundColor = _lib.SetImageBackgroundColor
SetImageBackgroundColor.restype = MagickBooleanType
SetImageBackgroundColor.argtypes = [POINTER(Image)]
SetImageClipMask = _lib.SetImageClipMask
SetImageClipMask.restype = MagickBooleanType
SetImageClipMask.argtypes = [POINTER(Image), POINTER(Image)]
SetImageColor = _lib.SetImageColor
SetImageColor.restype = MagickBooleanType
SetImageColor.argtypes = [POINTER(Image), POINTER(MagickPixelPacket)]
SetImageExtent = _lib.SetImageExtent
SetImageExtent.restype = MagickBooleanType
SetImageExtent.argtypes = [POINTER(Image), size_t, size_t]
SetImageInfo = _lib.SetImageInfo
SetImageInfo.restype = MagickBooleanType
SetImageInfo.argtypes = [POINTER(ImageInfo), c_uint, POINTER(ExceptionInfo)]
SetImageMask = _lib.SetImageMask
SetImageMask.restype = MagickBooleanType
SetImageMask.argtypes = [POINTER(Image), POINTER(Image)]
SetImageOpacity = _lib.SetImageOpacity
SetImageOpacity.restype = MagickBooleanType
SetImageOpacity.argtypes = [POINTER(Image), Quantum]
SetImageStorageClass = _lib.SetImageStorageClass
SetImageStorageClass.restype = MagickBooleanType
SetImageStorageClass.argtypes = [POINTER(Image), ClassType]
SetImageType = _lib.SetImageType
SetImageType.restype = MagickBooleanType
SetImageType.argtypes = [POINTER(Image), ImageType]
StripImage = _lib.StripImage
StripImage.restype = MagickBooleanType
StripImage.argtypes = [POINTER(Image)]
SyncImage = _lib.SyncImage
SyncImage.restype = MagickBooleanType
SyncImage.argtypes = [POINTER(Image)]
SyncImageSettings = _lib.SyncImageSettings
SyncImageSettings.restype = MagickBooleanType
SyncImageSettings.argtypes = [POINTER(ImageInfo), POINTER(Image)]
SyncImagesSettings = _lib.SyncImagesSettings
SyncImagesSettings.restype = MagickBooleanType
SyncImagesSettings.argtypes = [POINTER(ImageInfo), POINTER(Image)]
InterpretImageFilename = _lib.InterpretImageFilename
InterpretImageFilename.restype = size_t
InterpretImageFilename.argtypes = [POINTER(ImageInfo), POINTER(Image), STRING, c_int, STRING]
GetImageReferenceCount = _lib.GetImageReferenceCount
GetImageReferenceCount.restype = ssize_t
GetImageReferenceCount.argtypes = [POINTER(Image)]
GetImageVirtualPixelMethod = _lib.GetImageVirtualPixelMethod
GetImageVirtualPixelMethod.restype = VirtualPixelMethod
GetImageVirtualPixelMethod.argtypes = [POINTER(Image)]
SetImageVirtualPixelMethod = _lib.SetImageVirtualPixelMethod
SetImageVirtualPixelMethod.restype = VirtualPixelMethod
SetImageVirtualPixelMethod.argtypes = [POINTER(Image), VirtualPixelMethod]
AcquireNextImage = _lib.AcquireNextImage
AcquireNextImage.restype = None
AcquireNextImage.argtypes = [POINTER(ImageInfo), POINTER(Image)]
DestroyImagePixels = _lib.DestroyImagePixels
DestroyImagePixels.restype = None
DestroyImagePixels.argtypes = [POINTER(Image)]
DisassociateImageStream = _lib.DisassociateImageStream
DisassociateImageStream.restype = None
DisassociateImageStream.argtypes = [POINTER(Image)]
GetImageException = _lib.GetImageException
GetImageException.restype = None
GetImageException.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
GetImageInfo = _lib.GetImageInfo
GetImageInfo.restype = None
GetImageInfo.argtypes = [POINTER(ImageInfo)]
SetImageInfoBlob = _lib.SetImageInfoBlob
SetImageInfoBlob.restype = None
SetImageInfoBlob.argtypes = [POINTER(ImageInfo), c_void_p, size_t]
SetImageInfoFile = _lib.SetImageInfoFile
SetImageInfoFile.restype = None
SetImageInfoFile.argtypes = [POINTER(ImageInfo), POINTER(FILE)]

# values for enumeration 'DisposeType'
DisposeType = c_int # enum

# values for enumeration 'ImageLayerMethod'
ImageLayerMethod = c_int # enum
CoalesceImages = _lib.CoalesceImages
CoalesceImages.restype = POINTER(Image)
CoalesceImages.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
DisposeImages = _lib.DisposeImages
DisposeImages.restype = POINTER(Image)
DisposeImages.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
CompareImageLayers = _lib.CompareImageLayers
CompareImageLayers.restype = POINTER(Image)
CompareImageLayers.argtypes = [POINTER(Image), ImageLayerMethod, POINTER(ExceptionInfo)]
DeconstructImages = _lib.DeconstructImages
DeconstructImages.restype = POINTER(Image)
DeconstructImages.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
MergeImageLayers = _lib.MergeImageLayers
MergeImageLayers.restype = POINTER(Image)
MergeImageLayers.argtypes = [POINTER(Image), ImageLayerMethod, POINTER(ExceptionInfo)]
OptimizeImageLayers = _lib.OptimizeImageLayers
OptimizeImageLayers.restype = POINTER(Image)
OptimizeImageLayers.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
OptimizePlusImageLayers = _lib.OptimizePlusImageLayers
OptimizePlusImageLayers.restype = POINTER(Image)
OptimizePlusImageLayers.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
CompositeLayers = _lib.CompositeLayers
CompositeLayers.restype = None
CompositeLayers.argtypes = [POINTER(Image), CompositeOperator, POINTER(Image), ssize_t, ssize_t, POINTER(ExceptionInfo)]
OptimizeImageTransparency = _lib.OptimizeImageTransparency
OptimizeImageTransparency.restype = None
OptimizeImageTransparency.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
RemoveDuplicateLayers = _lib.RemoveDuplicateLayers
RemoveDuplicateLayers.restype = None
RemoveDuplicateLayers.argtypes = [POINTER(POINTER(Image)), POINTER(ExceptionInfo)]
RemoveZeroDelayLayers = _lib.RemoveZeroDelayLayers
RemoveZeroDelayLayers.restype = None
RemoveZeroDelayLayers.argtypes = [POINTER(POINTER(Image)), POINTER(ExceptionInfo)]
CloneImageList = _lib.CloneImageList
CloneImageList.restype = POINTER(Image)
CloneImageList.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
CloneImages = _lib.CloneImages
CloneImages.restype = POINTER(Image)
CloneImages.argtypes = [POINTER(Image), STRING, POINTER(ExceptionInfo)]
DestroyImageList = _lib.DestroyImageList
DestroyImageList.restype = POINTER(Image)
DestroyImageList.argtypes = [POINTER(Image)]
GetFirstImageInList = _lib.GetFirstImageInList
GetFirstImageInList.restype = POINTER(Image)
GetFirstImageInList.argtypes = [POINTER(Image)]
GetImageFromList = _lib.GetImageFromList
GetImageFromList.restype = POINTER(Image)
GetImageFromList.argtypes = [POINTER(Image), ssize_t]
GetLastImageInList = _lib.GetLastImageInList
GetLastImageInList.restype = POINTER(Image)
GetLastImageInList.argtypes = [POINTER(Image)]
GetNextImageInList = _lib.GetNextImageInList
GetNextImageInList.restype = POINTER(Image)
GetNextImageInList.argtypes = [POINTER(Image)]
GetPreviousImageInList = _lib.GetPreviousImageInList
GetPreviousImageInList.restype = POINTER(Image)
GetPreviousImageInList.argtypes = [POINTER(Image)]
ImageListToArray = _lib.ImageListToArray
ImageListToArray.restype = POINTER(POINTER(Image))
ImageListToArray.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
NewImageList = _lib.NewImageList
NewImageList.restype = POINTER(Image)
NewImageList.argtypes = []
RemoveImageFromList = _lib.RemoveImageFromList
RemoveImageFromList.restype = POINTER(Image)
RemoveImageFromList.argtypes = [POINTER(POINTER(Image))]
RemoveLastImageFromList = _lib.RemoveLastImageFromList
RemoveLastImageFromList.restype = POINTER(Image)
RemoveLastImageFromList.argtypes = [POINTER(POINTER(Image))]
RemoveFirstImageFromList = _lib.RemoveFirstImageFromList
RemoveFirstImageFromList.restype = POINTER(Image)
RemoveFirstImageFromList.argtypes = [POINTER(POINTER(Image))]
SpliceImageIntoList = _lib.SpliceImageIntoList
SpliceImageIntoList.restype = POINTER(Image)
SpliceImageIntoList.argtypes = [POINTER(POINTER(Image)), size_t, POINTER(Image)]
SplitImageList = _lib.SplitImageList
SplitImageList.restype = POINTER(Image)
SplitImageList.argtypes = [POINTER(Image)]
SyncNextImageInList = _lib.SyncNextImageInList
SyncNextImageInList.restype = POINTER(Image)
SyncNextImageInList.argtypes = [POINTER(Image)]
GetImageListLength = _lib.GetImageListLength
GetImageListLength.restype = size_t
GetImageListLength.argtypes = [POINTER(Image)]
GetImageIndexInList = _lib.GetImageIndexInList
GetImageIndexInList.restype = ssize_t
GetImageIndexInList.argtypes = [POINTER(Image)]
AppendImageToList = _lib.AppendImageToList
AppendImageToList.restype = None
AppendImageToList.argtypes = [POINTER(POINTER(Image)), POINTER(Image)]
DeleteImageFromList = _lib.DeleteImageFromList
DeleteImageFromList.restype = None
DeleteImageFromList.argtypes = [POINTER(POINTER(Image))]
DeleteImages = _lib.DeleteImages
DeleteImages.restype = None
DeleteImages.argtypes = [POINTER(POINTER(Image)), STRING, POINTER(ExceptionInfo)]
InsertImageInList = _lib.InsertImageInList
InsertImageInList.restype = None
InsertImageInList.argtypes = [POINTER(POINTER(Image)), POINTER(Image)]
PrependImageToList = _lib.PrependImageToList
PrependImageToList.restype = None
PrependImageToList.argtypes = [POINTER(POINTER(Image)), POINTER(Image)]
ReplaceImageInList = _lib.ReplaceImageInList
ReplaceImageInList.restype = None
ReplaceImageInList.argtypes = [POINTER(POINTER(Image)), POINTER(Image)]
ReverseImageList = _lib.ReverseImageList
ReverseImageList.restype = None
ReverseImageList.argtypes = [POINTER(POINTER(Image))]
SyncImageList = _lib.SyncImageList
SyncImageList.restype = None
SyncImageList.argtypes = [POINTER(Image)]
class _LocaleInfo(Structure):
    pass
LocaleInfo = _LocaleInfo
GetLocaleList = _lib.GetLocaleList
GetLocaleList.restype = POINTER(STRING)
GetLocaleList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
GetLocaleMessage = _lib.GetLocaleMessage
GetLocaleMessage.restype = STRING
GetLocaleMessage.argtypes = [STRING]
GetLocaleInfo_ = _lib.GetLocaleInfo_
GetLocaleInfo_.restype = POINTER(LocaleInfo)
GetLocaleInfo_.argtypes = [STRING, POINTER(ExceptionInfo)]
GetLocaleInfoList = _lib.GetLocaleInfoList
GetLocaleInfoList.restype = POINTER(POINTER(LocaleInfo))
GetLocaleInfoList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
DestroyLocaleOptions = _lib.DestroyLocaleOptions
DestroyLocaleOptions.restype = POINTER(LinkedListInfo)
DestroyLocaleOptions.argtypes = [POINTER(LinkedListInfo)]
GetLocaleOptions = _lib.GetLocaleOptions
GetLocaleOptions.restype = POINTER(LinkedListInfo)
GetLocaleOptions.argtypes = [STRING, POINTER(ExceptionInfo)]
ListLocaleInfo = _lib.ListLocaleInfo
ListLocaleInfo.restype = MagickBooleanType
ListLocaleInfo.argtypes = [POINTER(FILE), POINTER(ExceptionInfo)]
LocaleComponentGenesis = _lib.LocaleComponentGenesis
LocaleComponentGenesis.restype = MagickBooleanType
LocaleComponentGenesis.argtypes = []
LocaleComponentTerminus = _lib.LocaleComponentTerminus
LocaleComponentTerminus.restype = None
LocaleComponentTerminus.argtypes = []

# values for enumeration 'LogEventType'
LogEventType = c_int # enum
class _LogInfo(Structure):
    pass
LogInfo = _LogInfo
GetLogList = _lib.GetLogList
GetLogList.restype = POINTER(STRING)
GetLogList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
GetLogName = _lib.GetLogName
GetLogName.restype = STRING
GetLogName.argtypes = []
SetLogName = _lib.SetLogName
SetLogName.restype = STRING
SetLogName.argtypes = [STRING]
GetLogInfoList = _lib.GetLogInfoList
GetLogInfoList.restype = POINTER(POINTER(LogInfo))
GetLogInfoList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
SetLogEventMask = _lib.SetLogEventMask
SetLogEventMask.restype = LogEventType
SetLogEventMask.argtypes = [STRING]
IsEventLogging = _lib.IsEventLogging
IsEventLogging.restype = MagickBooleanType
IsEventLogging.argtypes = []
ListLogInfo = _lib.ListLogInfo
ListLogInfo.restype = MagickBooleanType
ListLogInfo.argtypes = [POINTER(FILE), POINTER(ExceptionInfo)]
LogComponentGenesis = _lib.LogComponentGenesis
LogComponentGenesis.restype = MagickBooleanType
LogComponentGenesis.argtypes = []
LogMagickEvent = _lib.LogMagickEvent
LogMagickEvent.restype = MagickBooleanType
LogMagickEvent.argtypes = [LogEventType, STRING, STRING, size_t, STRING]
LogMagickEventList = _lib.LogMagickEventList
LogMagickEventList.restype = MagickBooleanType
LogMagickEventList.argtypes = [LogEventType, STRING, STRING, size_t, STRING, POINTER(__va_list_tag)]
CloseMagickLog = _lib.CloseMagickLog
CloseMagickLog.restype = None
CloseMagickLog.argtypes = []
LogComponentTerminus = _lib.LogComponentTerminus
LogComponentTerminus.restype = None
LogComponentTerminus.argtypes = []
SetLogFormat = _lib.SetLogFormat
SetLogFormat.restype = None
SetLogFormat.argtypes = [STRING]
class _MagicInfo(Structure):
    pass
MagicInfo = _MagicInfo
GetMagicList = _lib.GetMagicList
GetMagicList.restype = POINTER(STRING)
GetMagicList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
GetMagicName = _lib.GetMagicName
GetMagicName.restype = STRING
GetMagicName.argtypes = [POINTER(MagicInfo)]
ListMagicInfo = _lib.ListMagicInfo
ListMagicInfo.restype = MagickBooleanType
ListMagicInfo.argtypes = [POINTER(FILE), POINTER(ExceptionInfo)]
MagicComponentGenesis = _lib.MagicComponentGenesis
MagicComponentGenesis.restype = MagickBooleanType
MagicComponentGenesis.argtypes = []
GetMagicInfo = _lib.GetMagicInfo
GetMagicInfo.restype = POINTER(MagicInfo)
GetMagicInfo.argtypes = [POINTER(c_ubyte), size_t, POINTER(ExceptionInfo)]
GetMagicInfoList = _lib.GetMagicInfoList
GetMagicInfoList.restype = POINTER(POINTER(MagicInfo))
GetMagicInfoList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
MagicComponentTerminus = _lib.MagicComponentTerminus
MagicComponentTerminus.restype = None
MagicComponentTerminus.argtypes = []
QuantumAny = MagickSizeType
class _BlobInfo(Structure):
    pass
BlobInfo = _BlobInfo

# values for enumeration 'MagickFormatType'
MagickFormatType = c_int # enum

# values for enumeration 'MagickThreadSupport'
MagickThreadSupport = c_int # enum
DecodeImageHandler = CFUNCTYPE(POINTER(Image), POINTER(ImageInfo), POINTER(ExceptionInfo))
EncodeImageHandler = CFUNCTYPE(MagickBooleanType, POINTER(ImageInfo), POINTER(Image))
IsImageFormatHandler = CFUNCTYPE(MagickBooleanType, POINTER(c_ubyte), size_t)
class _MagickInfo(Structure):
    pass
MagickInfo = _MagickInfo
GetMagickList = _lib.GetMagickList
GetMagickList.restype = POINTER(STRING)
GetMagickList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
GetMagickDescription = _lib.GetMagickDescription
GetMagickDescription.restype = STRING
GetMagickDescription.argtypes = [POINTER(MagickInfo)]
GetImageDecoder = _lib.GetImageDecoder
GetImageDecoder.restype = POINTER(DecodeImageHandler)
GetImageDecoder.argtypes = [POINTER(MagickInfo)]
GetImageEncoder = _lib.GetImageEncoder
GetImageEncoder.restype = POINTER(EncodeImageHandler)
GetImageEncoder.argtypes = [POINTER(MagickInfo)]
GetMagickPrecision = _lib.GetMagickPrecision
GetMagickPrecision.restype = c_int
GetMagickPrecision.argtypes = []
SetMagickPrecision = _lib.SetMagickPrecision
SetMagickPrecision.restype = c_int
SetMagickPrecision.argtypes = [c_int]
GetImageMagick = _lib.GetImageMagick
GetImageMagick.restype = MagickBooleanType
GetImageMagick.argtypes = [POINTER(c_ubyte), size_t, STRING]
GetMagickAdjoin = _lib.GetMagickAdjoin
GetMagickAdjoin.restype = MagickBooleanType
GetMagickAdjoin.argtypes = [POINTER(MagickInfo)]
GetMagickBlobSupport = _lib.GetMagickBlobSupport
GetMagickBlobSupport.restype = MagickBooleanType
GetMagickBlobSupport.argtypes = [POINTER(MagickInfo)]
GetMagickEndianSupport = _lib.GetMagickEndianSupport
GetMagickEndianSupport.restype = MagickBooleanType
GetMagickEndianSupport.argtypes = [POINTER(MagickInfo)]
GetMagickRawSupport = _lib.GetMagickRawSupport
GetMagickRawSupport.restype = MagickBooleanType
GetMagickRawSupport.argtypes = [POINTER(MagickInfo)]
GetMagickSeekableStream = _lib.GetMagickSeekableStream
GetMagickSeekableStream.restype = MagickBooleanType
GetMagickSeekableStream.argtypes = [POINTER(MagickInfo)]
IsMagickInstantiated = _lib.IsMagickInstantiated
IsMagickInstantiated.restype = MagickBooleanType
IsMagickInstantiated.argtypes = []
MagickComponentGenesis = _lib.MagickComponentGenesis
MagickComponentGenesis.restype = MagickBooleanType
MagickComponentGenesis.argtypes = []
UnregisterMagickInfo = _lib.UnregisterMagickInfo
UnregisterMagickInfo.restype = MagickBooleanType
UnregisterMagickInfo.argtypes = [STRING]
GetMagickInfo = _lib.GetMagickInfo
GetMagickInfo.restype = POINTER(MagickInfo)
GetMagickInfo.argtypes = [STRING, POINTER(ExceptionInfo)]
GetMagickInfoList = _lib.GetMagickInfoList
GetMagickInfoList.restype = POINTER(POINTER(MagickInfo))
GetMagickInfoList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
RegisterMagickInfo = _lib.RegisterMagickInfo
RegisterMagickInfo.restype = POINTER(MagickInfo)
RegisterMagickInfo.argtypes = [POINTER(MagickInfo)]
SetMagickInfo = _lib.SetMagickInfo
SetMagickInfo.restype = POINTER(MagickInfo)
SetMagickInfo.argtypes = [STRING]
GetMagickThreadSupport = _lib.GetMagickThreadSupport
GetMagickThreadSupport.restype = MagickStatusType
GetMagickThreadSupport.argtypes = [POINTER(MagickInfo)]
MagickComponentTerminus = _lib.MagickComponentTerminus
MagickComponentTerminus.restype = None
MagickComponentTerminus.argtypes = []
MagickCoreGenesis = _lib.MagickCoreGenesis
MagickCoreGenesis.restype = None
MagickCoreGenesis.argtypes = [STRING, MagickBooleanType]
MagickCoreTerminus = _lib.MagickCoreTerminus
MagickCoreTerminus.restype = None
MagickCoreTerminus.argtypes = []
AcquireMagickMatrix = _lib.AcquireMagickMatrix
AcquireMagickMatrix.restype = POINTER(POINTER(c_double))
AcquireMagickMatrix.argtypes = [size_t, size_t]
RelinquishMagickMatrix = _lib.RelinquishMagickMatrix
RelinquishMagickMatrix.restype = POINTER(POINTER(c_double))
RelinquishMagickMatrix.argtypes = [POINTER(POINTER(c_double)), size_t]
GaussJordanElimination = _lib.GaussJordanElimination
GaussJordanElimination.restype = MagickBooleanType
GaussJordanElimination.argtypes = [POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), size_t, size_t]
LeastSquaresAddTerms = _lib.LeastSquaresAddTerms
LeastSquaresAddTerms.restype = None
LeastSquaresAddTerms.argtypes = [POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), POINTER(c_double), POINTER(c_double), size_t, size_t]
AcquireMemoryHandler = CFUNCTYPE(c_void_p, size_t)
DestroyMemoryHandler = CFUNCTYPE(None, c_void_p)
ResizeMemoryHandler = CFUNCTYPE(c_void_p, c_void_p, size_t)
AcquireAlignedMemory = _lib.AcquireAlignedMemory
AcquireAlignedMemory.restype = c_void_p
AcquireAlignedMemory.argtypes = [size_t, size_t]
AcquireMagickMemory = _lib.AcquireMagickMemory
AcquireMagickMemory.restype = c_void_p
AcquireMagickMemory.argtypes = [size_t]
AcquireQuantumMemory = _lib.AcquireQuantumMemory
AcquireQuantumMemory.restype = c_void_p
AcquireQuantumMemory.argtypes = [size_t, size_t]
CopyMagickMemory = _lib.CopyMagickMemory
CopyMagickMemory.restype = c_void_p
CopyMagickMemory.argtypes = [c_void_p, c_void_p, size_t]
DestroyMagickMemory = _lib.DestroyMagickMemory
DestroyMagickMemory.restype = None
DestroyMagickMemory.argtypes = []
GetMagickMemoryMethods = _lib.GetMagickMemoryMethods
GetMagickMemoryMethods.restype = None
GetMagickMemoryMethods.argtypes = [POINTER(AcquireMemoryHandler), POINTER(ResizeMemoryHandler), POINTER(DestroyMemoryHandler)]
RelinquishAlignedMemory = _lib.RelinquishAlignedMemory
RelinquishAlignedMemory.restype = c_void_p
RelinquishAlignedMemory.argtypes = [c_void_p]
RelinquishMagickMemory = _lib.RelinquishMagickMemory
RelinquishMagickMemory.restype = c_void_p
RelinquishMagickMemory.argtypes = [c_void_p]
ResetMagickMemory = _lib.ResetMagickMemory
ResetMagickMemory.restype = c_void_p
ResetMagickMemory.argtypes = [c_void_p, c_int, size_t]
ResizeMagickMemory = _lib.ResizeMagickMemory
ResizeMagickMemory.restype = c_void_p
ResizeMagickMemory.argtypes = [c_void_p, size_t]
ResizeQuantumMemory = _lib.ResizeQuantumMemory
ResizeQuantumMemory.restype = c_void_p
ResizeQuantumMemory.argtypes = [c_void_p, size_t, size_t]
SetMagickMemoryMethods = _lib.SetMagickMemoryMethods
SetMagickMemoryMethods.restype = None
SetMagickMemoryMethods.argtypes = [AcquireMemoryHandler, ResizeMemoryHandler, DestroyMemoryHandler]
class _MimeInfo(Structure):
    pass
MimeInfo = _MimeInfo
GetMimeList = _lib.GetMimeList
GetMimeList.restype = POINTER(STRING)
GetMimeList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
MagickToMime = _lib.MagickToMime
MagickToMime.restype = STRING
MagickToMime.argtypes = [STRING]
GetMimeDescription = _lib.GetMimeDescription
GetMimeDescription.restype = STRING
GetMimeDescription.argtypes = [POINTER(MimeInfo)]
GetMimeType = _lib.GetMimeType
GetMimeType.restype = STRING
GetMimeType.argtypes = [POINTER(MimeInfo)]
ListMimeInfo = _lib.ListMimeInfo
ListMimeInfo.restype = MagickBooleanType
ListMimeInfo.argtypes = [POINTER(FILE), POINTER(ExceptionInfo)]
LoadMimeLists = _lib.LoadMimeLists
LoadMimeLists.restype = MagickBooleanType
LoadMimeLists.argtypes = [STRING, POINTER(ExceptionInfo)]
MimeComponentGenesis = _lib.MimeComponentGenesis
MimeComponentGenesis.restype = MagickBooleanType
MimeComponentGenesis.argtypes = []
GetMimeInfo = _lib.GetMimeInfo
GetMimeInfo.restype = POINTER(MimeInfo)
GetMimeInfo.argtypes = [STRING, POINTER(c_ubyte), size_t, POINTER(ExceptionInfo)]
GetMimeInfoList = _lib.GetMimeInfoList
GetMimeInfoList.restype = POINTER(POINTER(MimeInfo))
GetMimeInfoList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
MimeComponentTerminus = _lib.MimeComponentTerminus
MimeComponentTerminus.restype = None
MimeComponentTerminus.argtypes = []

# values for enumeration 'MagickModuleType'
MagickModuleType = c_int # enum
class _ModuleInfo(Structure):
    pass
ModuleInfo = _ModuleInfo
ImageFilterHandler = CFUNCTYPE(size_t, POINTER(POINTER(Image)), c_int, POINTER(STRING), POINTER(ExceptionInfo))
GetModuleList = _lib.GetModuleList
GetModuleList.restype = POINTER(STRING)
GetModuleList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
GetModuleInfoList = _lib.GetModuleInfoList
GetModuleInfoList.restype = POINTER(POINTER(ModuleInfo))
GetModuleInfoList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
InitializeModuleList = _lib.InitializeModuleList
InitializeModuleList.restype = MagickBooleanType
InitializeModuleList.argtypes = [POINTER(ExceptionInfo)]
InvokeDynamicImageFilter = _lib.InvokeDynamicImageFilter
InvokeDynamicImageFilter.restype = MagickBooleanType
InvokeDynamicImageFilter.argtypes = [STRING, POINTER(POINTER(Image)), c_int, POINTER(STRING), POINTER(ExceptionInfo)]
ListModuleInfo = _lib.ListModuleInfo
ListModuleInfo.restype = MagickBooleanType
ListModuleInfo.argtypes = [POINTER(FILE), POINTER(ExceptionInfo)]
ModuleComponentGenesis = _lib.ModuleComponentGenesis
ModuleComponentGenesis.restype = MagickBooleanType
ModuleComponentGenesis.argtypes = []
OpenModule = _lib.OpenModule
OpenModule.restype = MagickBooleanType
OpenModule.argtypes = [STRING, POINTER(ExceptionInfo)]
OpenModules = _lib.OpenModules
OpenModules.restype = MagickBooleanType
OpenModules.argtypes = [POINTER(ExceptionInfo)]
GetModuleInfo = _lib.GetModuleInfo
GetModuleInfo.restype = POINTER(ModuleInfo)
GetModuleInfo.argtypes = [STRING, POINTER(ExceptionInfo)]
DestroyModuleList = _lib.DestroyModuleList
DestroyModuleList.restype = None
DestroyModuleList.argtypes = []
ModuleComponentTerminus = _lib.ModuleComponentTerminus
ModuleComponentTerminus.restype = None
ModuleComponentTerminus.argtypes = []
RegisterStaticModules = _lib.RegisterStaticModules
RegisterStaticModules.restype = None
RegisterStaticModules.argtypes = []
UnregisterStaticModules = _lib.UnregisterStaticModules
UnregisterStaticModules.restype = None
UnregisterStaticModules.argtypes = []
MagickProgressMonitor = CFUNCTYPE(MagickBooleanType, STRING, MagickOffsetType, MagickSizeType, c_void_p)
SetImageProgressMonitor = _lib.SetImageProgressMonitor
SetImageProgressMonitor.restype = MagickProgressMonitor
SetImageProgressMonitor.argtypes = [POINTER(Image), MagickProgressMonitor, c_void_p]
SetImageInfoProgressMonitor = _lib.SetImageInfoProgressMonitor
SetImageInfoProgressMonitor.restype = MagickProgressMonitor
SetImageInfoProgressMonitor.argtypes = [POINTER(ImageInfo), MagickProgressMonitor, c_void_p]

# values for enumeration 'MontageMode'
MontageMode = c_int # enum
class _MontageInfo(Structure):
    pass
MontageInfo = _MontageInfo
MontageImages = _lib.MontageImages
MontageImages.restype = POINTER(Image)
MontageImages.argtypes = [POINTER(Image), POINTER(MontageInfo), POINTER(ExceptionInfo)]
MontageImageList = _lib.MontageImageList
MontageImageList.restype = POINTER(Image)
MontageImageList.argtypes = [POINTER(ImageInfo), POINTER(MontageInfo), POINTER(Image), POINTER(ExceptionInfo)]
CloneMontageInfo = _lib.CloneMontageInfo
CloneMontageInfo.restype = POINTER(MontageInfo)
CloneMontageInfo.argtypes = [POINTER(ImageInfo), POINTER(MontageInfo)]
DestroyMontageInfo = _lib.DestroyMontageInfo
DestroyMontageInfo.restype = POINTER(MontageInfo)
DestroyMontageInfo.argtypes = [POINTER(MontageInfo)]
GetMontageInfo = _lib.GetMontageInfo
GetMontageInfo.restype = None
GetMontageInfo.argtypes = [POINTER(ImageInfo), POINTER(MontageInfo)]

# values for enumeration 'KernelInfoType'
KernelInfoType = c_int # enum

# values for enumeration 'MorphologyMethod'
MorphologyMethod = c_int # enum
KernelInfo._fields_ = [
    ('type', KernelInfoType),
    ('width', size_t),
    ('height', size_t),
    ('x', ssize_t),
    ('y', ssize_t),
    ('values', POINTER(c_double)),
    ('minimum', c_double),
    ('maximum', c_double),
    ('negative_range', c_double),
    ('positive_range', c_double),
    ('angle', c_double),
    ('next', POINTER(KernelInfo)),
    ('signature', size_t),
]
AcquireKernelInfo = _lib.AcquireKernelInfo
AcquireKernelInfo.restype = POINTER(KernelInfo)
AcquireKernelInfo.argtypes = [STRING]
AcquireKernelBuiltIn = _lib.AcquireKernelBuiltIn
AcquireKernelBuiltIn.restype = POINTER(KernelInfo)
AcquireKernelBuiltIn.argtypes = [KernelInfoType, POINTER(GeometryInfo)]
CloneKernelInfo = _lib.CloneKernelInfo
CloneKernelInfo.restype = POINTER(KernelInfo)
CloneKernelInfo.argtypes = [POINTER(KernelInfo)]
DestroyKernelInfo = _lib.DestroyKernelInfo
DestroyKernelInfo.restype = POINTER(KernelInfo)
DestroyKernelInfo.argtypes = [POINTER(KernelInfo)]
MorphologyImage = _lib.MorphologyImage
MorphologyImage.restype = POINTER(Image)
MorphologyImage.argtypes = [POINTER(Image), MorphologyMethod, ssize_t, POINTER(KernelInfo), POINTER(ExceptionInfo)]
MorphologyImageChannel = _lib.MorphologyImageChannel
MorphologyImageChannel.restype = POINTER(Image)
MorphologyImageChannel.argtypes = [POINTER(Image), ChannelType, MorphologyMethod, ssize_t, POINTER(KernelInfo), POINTER(ExceptionInfo)]
ScaleGeometryKernelInfo = _lib.ScaleGeometryKernelInfo
ScaleGeometryKernelInfo.restype = None
ScaleGeometryKernelInfo.argtypes = [POINTER(KernelInfo), STRING]
ShowKernelInfo = _lib.ShowKernelInfo
ShowKernelInfo.restype = None
ShowKernelInfo.argtypes = [POINTER(KernelInfo)]

# values for enumeration 'MagickOption'
MagickOption = c_int # enum

# values for enumeration 'ValidateType'
ValidateType = c_int # enum
class _OptionInfo(Structure):
    pass
OptionInfo = _OptionInfo
GetMagickOptions = _lib.GetMagickOptions
GetMagickOptions.restype = POINTER(STRING)
GetMagickOptions.argtypes = [MagickOption]
GetNextImageOption = _lib.GetNextImageOption
GetNextImageOption.restype = STRING
GetNextImageOption.argtypes = [POINTER(ImageInfo)]
RemoveImageOption = _lib.RemoveImageOption
RemoveImageOption.restype = STRING
RemoveImageOption.argtypes = [POINTER(ImageInfo), STRING]
GetImageOption = _lib.GetImageOption
GetImageOption.restype = STRING
GetImageOption.argtypes = [POINTER(ImageInfo), STRING]
MagickOptionToMnemonic = _lib.MagickOptionToMnemonic
MagickOptionToMnemonic.restype = STRING
MagickOptionToMnemonic.argtypes = [MagickOption, ssize_t]
CloneImageOptions = _lib.CloneImageOptions
CloneImageOptions.restype = MagickBooleanType
CloneImageOptions.argtypes = [POINTER(ImageInfo), POINTER(ImageInfo)]
DefineImageOption = _lib.DefineImageOption
DefineImageOption.restype = MagickBooleanType
DefineImageOption.argtypes = [POINTER(ImageInfo), STRING]
DeleteImageOption = _lib.DeleteImageOption
DeleteImageOption.restype = MagickBooleanType
DeleteImageOption.argtypes = [POINTER(ImageInfo), STRING]
IsMagickOption = _lib.IsMagickOption
IsMagickOption.restype = MagickBooleanType
IsMagickOption.argtypes = [STRING]
ListMagickOptions = _lib.ListMagickOptions
ListMagickOptions.restype = MagickBooleanType
ListMagickOptions.argtypes = [POINTER(FILE), MagickOption, POINTER(ExceptionInfo)]
SetImageOption = _lib.SetImageOption
SetImageOption.restype = MagickBooleanType
SetImageOption.argtypes = [POINTER(ImageInfo), STRING, STRING]
ParseChannelOption = _lib.ParseChannelOption
ParseChannelOption.restype = ssize_t
ParseChannelOption.argtypes = [STRING]
ParseMagickOption = _lib.ParseMagickOption
ParseMagickOption.restype = ssize_t
ParseMagickOption.argtypes = [MagickOption, MagickBooleanType, STRING]
DestroyImageOptions = _lib.DestroyImageOptions
DestroyImageOptions.restype = None
DestroyImageOptions.argtypes = [POINTER(ImageInfo)]
ResetImageOptions = _lib.ResetImageOptions
ResetImageOptions.restype = None
ResetImageOptions.argtypes = [POINTER(ImageInfo)]
ResetImageOptionIterator = _lib.ResetImageOptionIterator
ResetImageOptionIterator.restype = None
ResetImageOptionIterator.argtypes = [POINTER(ImageInfo)]
OilPaintImage = _lib.OilPaintImage
OilPaintImage.restype = POINTER(Image)
OilPaintImage.argtypes = [POINTER(Image), c_double, POINTER(ExceptionInfo)]
FloodfillPaintImage = _lib.FloodfillPaintImage
FloodfillPaintImage.restype = MagickBooleanType
FloodfillPaintImage.argtypes = [POINTER(Image), ChannelType, POINTER(DrawInfo), POINTER(MagickPixelPacket), ssize_t, ssize_t, MagickBooleanType]
GradientImage = _lib.GradientImage
GradientImage.restype = MagickBooleanType
GradientImage.argtypes = [POINTER(Image), GradientType, SpreadMethod, POINTER(PixelPacket), POINTER(PixelPacket)]
OpaquePaintImage = _lib.OpaquePaintImage
OpaquePaintImage.restype = MagickBooleanType
OpaquePaintImage.argtypes = [POINTER(Image), POINTER(MagickPixelPacket), POINTER(MagickPixelPacket), MagickBooleanType]
OpaquePaintImageChannel = _lib.OpaquePaintImageChannel
OpaquePaintImageChannel.restype = MagickBooleanType
OpaquePaintImageChannel.argtypes = [POINTER(Image), ChannelType, POINTER(MagickPixelPacket), POINTER(MagickPixelPacket), MagickBooleanType]
TransparentPaintImage = _lib.TransparentPaintImage
TransparentPaintImage.restype = MagickBooleanType
TransparentPaintImage.argtypes = [POINTER(Image), POINTER(MagickPixelPacket), Quantum, MagickBooleanType]
TransparentPaintImageChroma = _lib.TransparentPaintImageChroma
TransparentPaintImageChroma.restype = MagickBooleanType
TransparentPaintImageChroma.argtypes = [POINTER(Image), POINTER(MagickPixelPacket), POINTER(MagickPixelPacket), Quantum, MagickBooleanType]
class _DoublePixelPacket(Structure):
    pass
DoublePixelPacket = _DoublePixelPacket
class _LongPixelPacket(Structure):
    pass
LongPixelPacket = _LongPixelPacket
ExportImagePixels = _lib.ExportImagePixels
ExportImagePixels.restype = MagickBooleanType
ExportImagePixels.argtypes = [POINTER(Image), ssize_t, ssize_t, size_t, size_t, STRING, StorageType, c_void_p, POINTER(ExceptionInfo)]
ImportImagePixels = _lib.ImportImagePixels
ImportImagePixels.restype = MagickBooleanType
ImportImagePixels.argtypes = [POINTER(Image), ssize_t, ssize_t, size_t, size_t, STRING, StorageType, c_void_p]
GetMagickPixelPacket = _lib.GetMagickPixelPacket
GetMagickPixelPacket.restype = None
GetMagickPixelPacket.argtypes = [POINTER(Image), POINTER(MagickPixelPacket)]

# values for enumeration 'PolicyDomain'
PolicyDomain = c_int # enum

# values for enumeration 'PolicyRights'
PolicyRights = c_int # enum
class _PolicyInfo(Structure):
    pass
PolicyInfo = _PolicyInfo
GetPolicyValue = _lib.GetPolicyValue
GetPolicyValue.restype = STRING
GetPolicyValue.argtypes = [STRING]
GetPolicyList = _lib.GetPolicyList
GetPolicyList.restype = POINTER(STRING)
GetPolicyList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
GetPolicyInfoList = _lib.GetPolicyInfoList
GetPolicyInfoList.restype = POINTER(POINTER(PolicyInfo))
GetPolicyInfoList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
IsRightsAuthorized = _lib.IsRightsAuthorized
IsRightsAuthorized.restype = MagickBooleanType
IsRightsAuthorized.argtypes = [PolicyDomain, PolicyRights, STRING]
ListPolicyInfo = _lib.ListPolicyInfo
ListPolicyInfo.restype = MagickBooleanType
ListPolicyInfo.argtypes = [POINTER(FILE), POINTER(ExceptionInfo)]
PolicyComponentGenesis = _lib.PolicyComponentGenesis
PolicyComponentGenesis.restype = MagickBooleanType
PolicyComponentGenesis.argtypes = []
PolicyComponentTerminus = _lib.PolicyComponentTerminus
PolicyComponentTerminus.restype = None
PolicyComponentTerminus.argtypes = []
GetImageTotalInkDensity = _lib.GetImageTotalInkDensity
GetImageTotalInkDensity.restype = c_double
GetImageTotalInkDensity.argtypes = [POINTER(Image)]
class _ProfileInfo(Structure):
    pass
ProfileInfo = _ProfileInfo

# values for enumeration 'RenderingIntent'
RenderingIntent = c_int # enum
GetNextImageProfile = _lib.GetNextImageProfile
GetNextImageProfile.restype = STRING
GetNextImageProfile.argtypes = [POINTER(Image)]
GetImageProfile = _lib.GetImageProfile
GetImageProfile.restype = POINTER(StringInfo)
GetImageProfile.argtypes = [POINTER(Image), STRING]
CloneImageProfiles = _lib.CloneImageProfiles
CloneImageProfiles.restype = MagickBooleanType
CloneImageProfiles.argtypes = [POINTER(Image), POINTER(Image)]
DeleteImageProfile = _lib.DeleteImageProfile
DeleteImageProfile.restype = MagickBooleanType
DeleteImageProfile.argtypes = [POINTER(Image), STRING]
ProfileImage = _lib.ProfileImage
ProfileImage.restype = MagickBooleanType
ProfileImage.argtypes = [POINTER(Image), STRING, c_void_p, size_t, MagickBooleanType]
SetImageProfile = _lib.SetImageProfile
SetImageProfile.restype = MagickBooleanType
SetImageProfile.argtypes = [POINTER(Image), STRING, POINTER(StringInfo)]
SyncImageProfiles = _lib.SyncImageProfiles
SyncImageProfiles.restype = MagickBooleanType
SyncImageProfiles.argtypes = [POINTER(Image)]
RemoveImageProfile = _lib.RemoveImageProfile
RemoveImageProfile.restype = POINTER(StringInfo)
RemoveImageProfile.argtypes = [POINTER(Image), STRING]
DestroyImageProfiles = _lib.DestroyImageProfiles
DestroyImageProfiles.restype = None
DestroyImageProfiles.argtypes = [POINTER(Image)]
ResetImageProfileIterator = _lib.ResetImageProfileIterator
ResetImageProfileIterator.restype = None
ResetImageProfileIterator.argtypes = [POINTER(Image)]
GetNextImageProperty = _lib.GetNextImageProperty
GetNextImageProperty.restype = STRING
GetNextImageProperty.argtypes = [POINTER(Image)]
InterpretImageProperties = _lib.InterpretImageProperties
InterpretImageProperties.restype = STRING
InterpretImageProperties.argtypes = [POINTER(ImageInfo), POINTER(Image), STRING]
RemoveImageProperty = _lib.RemoveImageProperty
RemoveImageProperty.restype = STRING
RemoveImageProperty.argtypes = [POINTER(Image), STRING]
GetImageProperty = _lib.GetImageProperty
GetImageProperty.restype = STRING
GetImageProperty.argtypes = [POINTER(Image), STRING]
GetMagickProperty = _lib.GetMagickProperty
GetMagickProperty.restype = STRING
GetMagickProperty.argtypes = [POINTER(ImageInfo), POINTER(Image), STRING]
CloneImageProperties = _lib.CloneImageProperties
CloneImageProperties.restype = MagickBooleanType
CloneImageProperties.argtypes = [POINTER(Image), POINTER(Image)]
DefineImageProperty = _lib.DefineImageProperty
DefineImageProperty.restype = MagickBooleanType
DefineImageProperty.argtypes = [POINTER(Image), STRING]
DeleteImageProperty = _lib.DeleteImageProperty
DeleteImageProperty.restype = MagickBooleanType
DeleteImageProperty.argtypes = [POINTER(Image), STRING]
FormatImageProperty = _lib.FormatImageProperty
FormatImageProperty.restype = MagickBooleanType
FormatImageProperty.argtypes = [POINTER(Image), STRING, STRING]
FormatImagePropertyList = _lib.FormatImagePropertyList
FormatImagePropertyList.restype = MagickBooleanType
FormatImagePropertyList.argtypes = [POINTER(Image), STRING, STRING, POINTER(__va_list_tag)]
SetImageProperty = _lib.SetImageProperty
SetImageProperty.restype = MagickBooleanType
SetImageProperty.argtypes = [POINTER(Image), STRING, STRING]
DestroyImageProperties = _lib.DestroyImageProperties
DestroyImageProperties.restype = None
DestroyImageProperties.argtypes = [POINTER(Image)]
ResetImagePropertyIterator = _lib.ResetImagePropertyIterator
ResetImagePropertyIterator.restype = None
ResetImagePropertyIterator.argtypes = [POINTER(Image)]

# values for enumeration 'DitherMethod'
DitherMethod = c_int # enum
CompressImageColormap = _lib.CompressImageColormap
CompressImageColormap.restype = MagickBooleanType
CompressImageColormap.argtypes = [POINTER(Image)]
GetImageQuantizeError = _lib.GetImageQuantizeError
GetImageQuantizeError.restype = MagickBooleanType
GetImageQuantizeError.argtypes = [POINTER(Image)]
PosterizeImage = _lib.PosterizeImage
PosterizeImage.restype = MagickBooleanType
PosterizeImage.argtypes = [POINTER(Image), size_t, MagickBooleanType]
QuantizeImage = _lib.QuantizeImage
QuantizeImage.restype = MagickBooleanType
QuantizeImage.argtypes = [POINTER(QuantizeInfo), POINTER(Image)]
QuantizeImages = _lib.QuantizeImages
QuantizeImages.restype = MagickBooleanType
QuantizeImages.argtypes = [POINTER(QuantizeInfo), POINTER(Image)]
RemapImage = _lib.RemapImage
RemapImage.restype = MagickBooleanType
RemapImage.argtypes = [POINTER(QuantizeInfo), POINTER(Image), POINTER(Image)]
RemapImages = _lib.RemapImages
RemapImages.restype = MagickBooleanType
RemapImages.argtypes = [POINTER(QuantizeInfo), POINTER(Image), POINTER(Image)]
AcquireQuantizeInfo = _lib.AcquireQuantizeInfo
AcquireQuantizeInfo.restype = POINTER(QuantizeInfo)
AcquireQuantizeInfo.argtypes = [POINTER(ImageInfo)]
CloneQuantizeInfo = _lib.CloneQuantizeInfo
CloneQuantizeInfo.restype = POINTER(QuantizeInfo)
CloneQuantizeInfo.argtypes = [POINTER(QuantizeInfo)]
DestroyQuantizeInfo = _lib.DestroyQuantizeInfo
DestroyQuantizeInfo.restype = POINTER(QuantizeInfo)
DestroyQuantizeInfo.argtypes = [POINTER(QuantizeInfo)]
GetQuantizeInfo = _lib.GetQuantizeInfo
GetQuantizeInfo.restype = None
GetQuantizeInfo.argtypes = [POINTER(QuantizeInfo)]

# values for enumeration 'EndianType'
EndianType = c_int # enum

# values for enumeration 'QuantumAlphaType'
QuantumAlphaType = c_int # enum

# values for enumeration 'QuantumFormatType'
QuantumFormatType = c_int # enum
class _QuantumInfo(Structure):
    pass
QuantumInfo = _QuantumInfo
SetQuantumDepth = _lib.SetQuantumDepth
SetQuantumDepth.restype = MagickBooleanType
SetQuantumDepth.argtypes = [POINTER(Image), POINTER(QuantumInfo), size_t]
SetQuantumFormat = _lib.SetQuantumFormat
SetQuantumFormat.restype = MagickBooleanType
SetQuantumFormat.argtypes = [POINTER(Image), POINTER(QuantumInfo), QuantumFormatType]
SetQuantumPad = _lib.SetQuantumPad
SetQuantumPad.restype = MagickBooleanType
SetQuantumPad.argtypes = [POINTER(Image), POINTER(QuantumInfo), size_t]
AcquireQuantumInfo = _lib.AcquireQuantumInfo
AcquireQuantumInfo.restype = POINTER(QuantumInfo)
AcquireQuantumInfo.argtypes = [POINTER(ImageInfo), POINTER(Image)]
DestroyQuantumInfo = _lib.DestroyQuantumInfo
DestroyQuantumInfo.restype = POINTER(QuantumInfo)
DestroyQuantumInfo.argtypes = [POINTER(QuantumInfo)]
GetQuantumType = _lib.GetQuantumType
GetQuantumType.restype = QuantumType
GetQuantumType.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
ExportQuantumPixels = _lib.ExportQuantumPixels
ExportQuantumPixels.restype = size_t
ExportQuantumPixels.argtypes = [POINTER(Image), POINTER(CacheView), POINTER(QuantumInfo), QuantumType, POINTER(c_ubyte), POINTER(ExceptionInfo)]
GetQuantumExtent = _lib.GetQuantumExtent
GetQuantumExtent.restype = size_t
GetQuantumExtent.argtypes = [POINTER(Image), POINTER(QuantumInfo), QuantumType]
ImportQuantumPixels = _lib.ImportQuantumPixels
ImportQuantumPixels.restype = size_t
ImportQuantumPixels.argtypes = [POINTER(Image), POINTER(CacheView), POINTER(QuantumInfo), QuantumType, POINTER(c_ubyte), POINTER(ExceptionInfo)]
GetQuantumPixels = _lib.GetQuantumPixels
GetQuantumPixels.restype = POINTER(c_ubyte)
GetQuantumPixels.argtypes = [POINTER(QuantumInfo)]
GetQuantumInfo = _lib.GetQuantumInfo
GetQuantumInfo.restype = None
GetQuantumInfo.argtypes = [POINTER(ImageInfo), POINTER(QuantumInfo)]
SetQuantumAlphaType = _lib.SetQuantumAlphaType
SetQuantumAlphaType.restype = None
SetQuantumAlphaType.argtypes = [POINTER(QuantumInfo), QuantumAlphaType]
SetQuantumImageType = _lib.SetQuantumImageType
SetQuantumImageType.restype = None
SetQuantumImageType.argtypes = [POINTER(Image), QuantumType]
SetQuantumMinIsWhite = _lib.SetQuantumMinIsWhite
SetQuantumMinIsWhite.restype = None
SetQuantumMinIsWhite.argtypes = [POINTER(QuantumInfo), MagickBooleanType]
SetQuantumPack = _lib.SetQuantumPack
SetQuantumPack.restype = None
SetQuantumPack.argtypes = [POINTER(QuantumInfo), MagickBooleanType]
SetQuantumQuantum = _lib.SetQuantumQuantum
SetQuantumQuantum.restype = None
SetQuantumQuantum.argtypes = [POINTER(QuantumInfo), size_t]
SetQuantumScale = _lib.SetQuantumScale
SetQuantumScale.restype = None
SetQuantumScale.argtypes = [POINTER(QuantumInfo), c_double]
GetRandomValue = _lib.GetRandomValue
GetRandomValue.restype = c_double
GetRandomValue.argtypes = [POINTER(RandomInfo)]
GetPseudoRandomValue = _lib.GetPseudoRandomValue
GetPseudoRandomValue.restype = c_double
GetPseudoRandomValue.argtypes = [POINTER(RandomInfo)]
RandomComponentGenesis = _lib.RandomComponentGenesis
RandomComponentGenesis.restype = MagickBooleanType
RandomComponentGenesis.argtypes = []
AcquireRandomInfo = _lib.AcquireRandomInfo
AcquireRandomInfo.restype = POINTER(RandomInfo)
AcquireRandomInfo.argtypes = []
DestroyRandomInfo = _lib.DestroyRandomInfo
DestroyRandomInfo.restype = POINTER(RandomInfo)
DestroyRandomInfo.argtypes = [POINTER(RandomInfo)]
GetRandomKey = _lib.GetRandomKey
GetRandomKey.restype = POINTER(StringInfo)
GetRandomKey.argtypes = [POINTER(RandomInfo), size_t]
RandomComponentTerminus = _lib.RandomComponentTerminus
RandomComponentTerminus.restype = None
RandomComponentTerminus.argtypes = []
SeedPseudoRandomGenerator = _lib.SeedPseudoRandomGenerator
SeedPseudoRandomGenerator.restype = None
SeedPseudoRandomGenerator.argtypes = [size_t]
SetRandomKey = _lib.SetRandomKey
SetRandomKey.restype = None
SetRandomKey.argtypes = [POINTER(RandomInfo), size_t, POINTER(c_ubyte)]
SetRandomTrueRandom = _lib.SetRandomTrueRandom
SetRandomTrueRandom.restype = None
SetRandomTrueRandom.argtypes = [MagickBooleanType]
GetNextImageRegistry = _lib.GetNextImageRegistry
GetNextImageRegistry.restype = STRING
GetNextImageRegistry.argtypes = []
DefineImageRegistry = _lib.DefineImageRegistry
DefineImageRegistry.restype = MagickBooleanType
DefineImageRegistry.argtypes = [RegistryType, STRING, POINTER(ExceptionInfo)]
DeleteImageRegistry = _lib.DeleteImageRegistry
DeleteImageRegistry.restype = MagickBooleanType
DeleteImageRegistry.argtypes = [STRING]
RegistryComponentGenesis = _lib.RegistryComponentGenesis
RegistryComponentGenesis.restype = MagickBooleanType
RegistryComponentGenesis.argtypes = []
SetImageRegistry = _lib.SetImageRegistry
SetImageRegistry.restype = MagickBooleanType
SetImageRegistry.argtypes = [RegistryType, STRING, c_void_p, POINTER(ExceptionInfo)]
GetImageRegistry = _lib.GetImageRegistry
GetImageRegistry.restype = c_void_p
GetImageRegistry.argtypes = [RegistryType, STRING, POINTER(ExceptionInfo)]
RegistryComponentTerminus = _lib.RegistryComponentTerminus
RegistryComponentTerminus.restype = None
RegistryComponentTerminus.argtypes = []
RemoveImageRegistry = _lib.RemoveImageRegistry
RemoveImageRegistry.restype = c_void_p
RemoveImageRegistry.argtypes = [STRING]
ResetImageRegistryIterator = _lib.ResetImageRegistryIterator
ResetImageRegistryIterator.restype = None
ResetImageRegistryIterator.argtypes = []

# values for enumeration 'FilterTypes'
FilterTypes = c_int # enum
class _ResampleFilter(Structure):
    pass
ResampleFilter = _ResampleFilter
ResamplePixelColor = _lib.ResamplePixelColor
ResamplePixelColor.restype = MagickBooleanType
ResamplePixelColor.argtypes = [POINTER(ResampleFilter), c_double, c_double, POINTER(MagickPixelPacket)]
SetResampleFilterInterpolateMethod = _lib.SetResampleFilterInterpolateMethod
SetResampleFilterInterpolateMethod.restype = MagickBooleanType
SetResampleFilterInterpolateMethod.argtypes = [POINTER(ResampleFilter), InterpolatePixelMethod]
SetResampleFilterVirtualPixelMethod = _lib.SetResampleFilterVirtualPixelMethod
SetResampleFilterVirtualPixelMethod.restype = MagickBooleanType
SetResampleFilterVirtualPixelMethod.argtypes = [POINTER(ResampleFilter), VirtualPixelMethod]
AcquireResampleFilter = _lib.AcquireResampleFilter
AcquireResampleFilter.restype = POINTER(ResampleFilter)
AcquireResampleFilter.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
DestroyResampleFilter = _lib.DestroyResampleFilter
DestroyResampleFilter.restype = POINTER(ResampleFilter)
DestroyResampleFilter.argtypes = [POINTER(ResampleFilter)]
ScaleResampleFilter = _lib.ScaleResampleFilter
ScaleResampleFilter.restype = None
ScaleResampleFilter.argtypes = [POINTER(ResampleFilter), c_double, c_double, c_double, c_double]
SetResampleFilter = _lib.SetResampleFilter
SetResampleFilter.restype = None
SetResampleFilter.argtypes = [POINTER(ResampleFilter), FilterTypes, c_double]
AdaptiveResizeImage = _lib.AdaptiveResizeImage
AdaptiveResizeImage.restype = POINTER(Image)
AdaptiveResizeImage.argtypes = [POINTER(Image), size_t, size_t, POINTER(ExceptionInfo)]
LiquidRescaleImage = _lib.LiquidRescaleImage
LiquidRescaleImage.restype = POINTER(Image)
LiquidRescaleImage.argtypes = [POINTER(Image), size_t, size_t, c_double, c_double, POINTER(ExceptionInfo)]
MagnifyImage = _lib.MagnifyImage
MagnifyImage.restype = POINTER(Image)
MagnifyImage.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
MinifyImage = _lib.MinifyImage
MinifyImage.restype = POINTER(Image)
MinifyImage.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
ResampleImage = _lib.ResampleImage
ResampleImage.restype = POINTER(Image)
ResampleImage.argtypes = [POINTER(Image), c_double, c_double, FilterTypes, c_double, POINTER(ExceptionInfo)]
ResizeImage = _lib.ResizeImage
ResizeImage.restype = POINTER(Image)
ResizeImage.argtypes = [POINTER(Image), size_t, size_t, FilterTypes, c_double, POINTER(ExceptionInfo)]
SampleImage = _lib.SampleImage
SampleImage.restype = POINTER(Image)
SampleImage.argtypes = [POINTER(Image), size_t, size_t, POINTER(ExceptionInfo)]
ScaleImage = _lib.ScaleImage
ScaleImage.restype = POINTER(Image)
ScaleImage.argtypes = [POINTER(Image), size_t, size_t, POINTER(ExceptionInfo)]
ThumbnailImage = _lib.ThumbnailImage
ThumbnailImage.restype = POINTER(Image)
ThumbnailImage.argtypes = [POINTER(Image), size_t, size_t, POINTER(ExceptionInfo)]
ZoomImage = _lib.ZoomImage
ZoomImage.restype = POINTER(Image)
ZoomImage.argtypes = [POINTER(Image), size_t, size_t, POINTER(ExceptionInfo)]

# values for enumeration 'ResourceType'
ResourceType = c_int # enum
AcquireUniqueFileResource = _lib.AcquireUniqueFileResource
AcquireUniqueFileResource.restype = c_int
AcquireUniqueFileResource.argtypes = [STRING]
AcquireMagickResource = _lib.AcquireMagickResource
AcquireMagickResource.restype = MagickBooleanType
AcquireMagickResource.argtypes = [ResourceType, MagickSizeType]
ListMagickResourceInfo = _lib.ListMagickResourceInfo
ListMagickResourceInfo.restype = MagickBooleanType
ListMagickResourceInfo.argtypes = [POINTER(FILE), POINTER(ExceptionInfo)]
RelinquishUniqueFileResource = _lib.RelinquishUniqueFileResource
RelinquishUniqueFileResource.restype = MagickBooleanType
RelinquishUniqueFileResource.argtypes = [STRING]
ResourceComponentGenesis = _lib.ResourceComponentGenesis
ResourceComponentGenesis.restype = MagickBooleanType
ResourceComponentGenesis.argtypes = []
SetMagickResourceLimit = _lib.SetMagickResourceLimit
SetMagickResourceLimit.restype = MagickBooleanType
SetMagickResourceLimit.argtypes = [ResourceType, MagickSizeType]
GetMagickResource = _lib.GetMagickResource
GetMagickResource.restype = MagickSizeType
GetMagickResource.argtypes = [ResourceType]
GetMagickResourceLimit = _lib.GetMagickResourceLimit
GetMagickResourceLimit.restype = MagickSizeType
GetMagickResourceLimit.argtypes = [ResourceType]
AsynchronousResourceComponentTerminus = _lib.AsynchronousResourceComponentTerminus
AsynchronousResourceComponentTerminus.restype = None
AsynchronousResourceComponentTerminus.argtypes = []
RelinquishMagickResource = _lib.RelinquishMagickResource
RelinquishMagickResource.restype = None
RelinquishMagickResource.argtypes = [ResourceType, MagickSizeType]
ResourceComponentTerminus = _lib.ResourceComponentTerminus
ResourceComponentTerminus.restype = None
ResourceComponentTerminus.argtypes = []
GetImageDynamicThreshold = _lib.GetImageDynamicThreshold
GetImageDynamicThreshold.restype = MagickBooleanType
GetImageDynamicThreshold.argtypes = [POINTER(Image), c_double, c_double, POINTER(MagickPixelPacket), POINTER(ExceptionInfo)]
SegmentImage = _lib.SegmentImage
SegmentImage.restype = MagickBooleanType
SegmentImage.argtypes = [POINTER(Image), ColorspaceType, MagickBooleanType, c_double, c_double]
SemaphoreInfo._fields_ = [
]
SemaphoreComponentGenesis = _lib.SemaphoreComponentGenesis
SemaphoreComponentGenesis.restype = MagickBooleanType
SemaphoreComponentGenesis.argtypes = []
AllocateSemaphoreInfo = _lib.AllocateSemaphoreInfo
AllocateSemaphoreInfo.restype = POINTER(SemaphoreInfo)
AllocateSemaphoreInfo.argtypes = []
AcquireSemaphoreInfo = _lib.AcquireSemaphoreInfo
AcquireSemaphoreInfo.restype = None
AcquireSemaphoreInfo.argtypes = [POINTER(POINTER(SemaphoreInfo))]
DestroySemaphoreInfo = _lib.DestroySemaphoreInfo
DestroySemaphoreInfo.restype = None
DestroySemaphoreInfo.argtypes = [POINTER(POINTER(SemaphoreInfo))]
LockSemaphoreInfo = _lib.LockSemaphoreInfo
LockSemaphoreInfo.restype = None
LockSemaphoreInfo.argtypes = [POINTER(SemaphoreInfo)]
RelinquishSemaphoreInfo = _lib.RelinquishSemaphoreInfo
RelinquishSemaphoreInfo.restype = None
RelinquishSemaphoreInfo.argtypes = [POINTER(SemaphoreInfo)]
SemaphoreComponentTerminus = _lib.SemaphoreComponentTerminus
SemaphoreComponentTerminus.restype = None
SemaphoreComponentTerminus.argtypes = []
UnlockSemaphoreInfo = _lib.UnlockSemaphoreInfo
UnlockSemaphoreInfo.restype = None
UnlockSemaphoreInfo.argtypes = [POINTER(SemaphoreInfo)]
AffineTransformImage = _lib.AffineTransformImage
AffineTransformImage.restype = POINTER(Image)
AffineTransformImage.argtypes = [POINTER(Image), POINTER(AffineMatrix), POINTER(ExceptionInfo)]
DeskewImage = _lib.DeskewImage
DeskewImage.restype = POINTER(Image)
DeskewImage.argtypes = [POINTER(Image), c_double, POINTER(ExceptionInfo)]
RotateImage = _lib.RotateImage
RotateImage.restype = POINTER(Image)
RotateImage.argtypes = [POINTER(Image), c_double, POINTER(ExceptionInfo)]
ShearImage = _lib.ShearImage
ShearImage.restype = POINTER(Image)
ShearImage.argtypes = [POINTER(Image), c_double, c_double, POINTER(ExceptionInfo)]
SignatureImage = _lib.SignatureImage
SignatureImage.restype = MagickBooleanType
SignatureImage.argtypes = [POINTER(Image)]
class _SplayTreeInfo(Structure):
    pass
SplayTreeInfo = _SplayTreeInfo
AddValueToSplayTree = _lib.AddValueToSplayTree
AddValueToSplayTree.restype = MagickBooleanType
AddValueToSplayTree.argtypes = [POINTER(SplayTreeInfo), c_void_p, c_void_p]
DeleteNodeByValueFromSplayTree = _lib.DeleteNodeByValueFromSplayTree
DeleteNodeByValueFromSplayTree.restype = MagickBooleanType
DeleteNodeByValueFromSplayTree.argtypes = [POINTER(SplayTreeInfo), c_void_p]
DeleteNodeFromSplayTree = _lib.DeleteNodeFromSplayTree
DeleteNodeFromSplayTree.restype = MagickBooleanType
DeleteNodeFromSplayTree.argtypes = [POINTER(SplayTreeInfo), c_void_p]
GetNextKeyInSplayTree = _lib.GetNextKeyInSplayTree
GetNextKeyInSplayTree.restype = c_void_p
GetNextKeyInSplayTree.argtypes = [POINTER(SplayTreeInfo)]
GetNextValueInSplayTree = _lib.GetNextValueInSplayTree
GetNextValueInSplayTree.restype = c_void_p
GetNextValueInSplayTree.argtypes = [POINTER(SplayTreeInfo)]
GetValueFromSplayTree = _lib.GetValueFromSplayTree
GetValueFromSplayTree.restype = c_void_p
GetValueFromSplayTree.argtypes = [POINTER(SplayTreeInfo), c_void_p]
CompareSplayTreeString = _lib.CompareSplayTreeString
CompareSplayTreeString.restype = c_int
CompareSplayTreeString.argtypes = [c_void_p, c_void_p]
CompareSplayTreeStringInfo = _lib.CompareSplayTreeStringInfo
CompareSplayTreeStringInfo.restype = c_int
CompareSplayTreeStringInfo.argtypes = [c_void_p, c_void_p]
CloneSplayTree = _lib.CloneSplayTree
CloneSplayTree.restype = POINTER(SplayTreeInfo)
CloneSplayTree.argtypes = [POINTER(SplayTreeInfo), CFUNCTYPE(c_void_p, c_void_p), CFUNCTYPE(c_void_p, c_void_p)]
DestroySplayTree = _lib.DestroySplayTree
DestroySplayTree.restype = POINTER(SplayTreeInfo)
DestroySplayTree.argtypes = [POINTER(SplayTreeInfo)]
NewSplayTree = _lib.NewSplayTree
NewSplayTree.restype = POINTER(SplayTreeInfo)
NewSplayTree.argtypes = [CFUNCTYPE(c_int, c_void_p, c_void_p), CFUNCTYPE(c_void_p, c_void_p), CFUNCTYPE(c_void_p, c_void_p)]
GetNumberOfNodesInSplayTree = _lib.GetNumberOfNodesInSplayTree
GetNumberOfNodesInSplayTree.restype = size_t
GetNumberOfNodesInSplayTree.argtypes = [POINTER(SplayTreeInfo)]
RemoveNodeByValueFromSplayTree = _lib.RemoveNodeByValueFromSplayTree
RemoveNodeByValueFromSplayTree.restype = c_void_p
RemoveNodeByValueFromSplayTree.argtypes = [POINTER(SplayTreeInfo), c_void_p]
RemoveNodeFromSplayTree = _lib.RemoveNodeFromSplayTree
RemoveNodeFromSplayTree.restype = c_void_p
RemoveNodeFromSplayTree.argtypes = [POINTER(SplayTreeInfo), c_void_p]
ResetSplayTree = _lib.ResetSplayTree
ResetSplayTree.restype = None
ResetSplayTree.argtypes = [POINTER(SplayTreeInfo)]
ResetSplayTreeIterator = _lib.ResetSplayTreeIterator
ResetSplayTreeIterator.restype = None
ResetSplayTreeIterator.argtypes = [POINTER(SplayTreeInfo)]
class _ChannelStatistics(Structure):
    pass
ChannelStatistics = _ChannelStatistics

# values for enumeration 'MagickEvaluateOperator'
MagickEvaluateOperator = c_int # enum

# values for enumeration 'MagickFunction'
MagickFunction = c_int # enum
GetImageChannelStatistics = _lib.GetImageChannelStatistics
GetImageChannelStatistics.restype = POINTER(ChannelStatistics)
GetImageChannelStatistics.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
EvaluateImages = _lib.EvaluateImages
EvaluateImages.restype = POINTER(Image)
EvaluateImages.argtypes = [POINTER(Image), MagickEvaluateOperator, POINTER(ExceptionInfo)]
EvaluateImage = _lib.EvaluateImage
EvaluateImage.restype = MagickBooleanType
EvaluateImage.argtypes = [POINTER(Image), MagickEvaluateOperator, c_double, POINTER(ExceptionInfo)]
EvaluateImageChannel = _lib.EvaluateImageChannel
EvaluateImageChannel.restype = MagickBooleanType
EvaluateImageChannel.argtypes = [POINTER(Image), ChannelType, MagickEvaluateOperator, c_double, POINTER(ExceptionInfo)]
FunctionImage = _lib.FunctionImage
FunctionImage.restype = MagickBooleanType
FunctionImage.argtypes = [POINTER(Image), MagickFunction, size_t, POINTER(c_double), POINTER(ExceptionInfo)]
FunctionImageChannel = _lib.FunctionImageChannel
FunctionImageChannel.restype = MagickBooleanType
FunctionImageChannel.argtypes = [POINTER(Image), ChannelType, MagickFunction, size_t, POINTER(c_double), POINTER(ExceptionInfo)]
GetImageChannelExtrema = _lib.GetImageChannelExtrema
GetImageChannelExtrema.restype = MagickBooleanType
GetImageChannelExtrema.argtypes = [POINTER(Image), ChannelType, POINTER(size_t), POINTER(size_t), POINTER(ExceptionInfo)]
GetImageChannelMean = _lib.GetImageChannelMean
GetImageChannelMean.restype = MagickBooleanType
GetImageChannelMean.argtypes = [POINTER(Image), ChannelType, POINTER(c_double), POINTER(c_double), POINTER(ExceptionInfo)]
GetImageChannelKurtosis = _lib.GetImageChannelKurtosis
GetImageChannelKurtosis.restype = MagickBooleanType
GetImageChannelKurtosis.argtypes = [POINTER(Image), ChannelType, POINTER(c_double), POINTER(c_double), POINTER(ExceptionInfo)]
GetImageChannelRange = _lib.GetImageChannelRange
GetImageChannelRange.restype = MagickBooleanType
GetImageChannelRange.argtypes = [POINTER(Image), ChannelType, POINTER(c_double), POINTER(c_double), POINTER(ExceptionInfo)]
GetImageExtrema = _lib.GetImageExtrema
GetImageExtrema.restype = MagickBooleanType
GetImageExtrema.argtypes = [POINTER(Image), POINTER(size_t), POINTER(size_t), POINTER(ExceptionInfo)]
GetImageRange = _lib.GetImageRange
GetImageRange.restype = MagickBooleanType
GetImageRange.argtypes = [POINTER(Image), POINTER(c_double), POINTER(c_double), POINTER(ExceptionInfo)]
GetImageMean = _lib.GetImageMean
GetImageMean.restype = MagickBooleanType
GetImageMean.argtypes = [POINTER(Image), POINTER(c_double), POINTER(c_double), POINTER(ExceptionInfo)]
GetImageKurtosis = _lib.GetImageKurtosis
GetImageKurtosis.restype = MagickBooleanType
GetImageKurtosis.argtypes = [POINTER(Image), POINTER(c_double), POINTER(c_double), POINTER(ExceptionInfo)]
ReadStream = _lib.ReadStream
ReadStream.restype = POINTER(Image)
ReadStream.argtypes = [POINTER(ImageInfo), StreamHandler, POINTER(ExceptionInfo)]
WriteStream = _lib.WriteStream
WriteStream.restype = MagickBooleanType
WriteStream.argtypes = [POINTER(ImageInfo), POINTER(Image), StreamHandler]
AcquireString = _lib.AcquireString
AcquireString.restype = STRING
AcquireString.argtypes = [STRING]
CloneString = _lib.CloneString
CloneString.restype = STRING
CloneString.argtypes = [POINTER(STRING), STRING]
ConstantString = _lib.ConstantString
ConstantString.restype = STRING
ConstantString.argtypes = [STRING]
DestroyString = _lib.DestroyString
DestroyString.restype = STRING
DestroyString.argtypes = [STRING]
DestroyStringList = _lib.DestroyStringList
DestroyStringList.restype = POINTER(STRING)
DestroyStringList.argtypes = [POINTER(STRING)]
EscapeString = _lib.EscapeString
EscapeString.restype = STRING
EscapeString.argtypes = [STRING, c_char]
FileToString = _lib.FileToString
FileToString.restype = STRING
FileToString.argtypes = [STRING, size_t, POINTER(ExceptionInfo)]
GetEnvironmentValue = _lib.GetEnvironmentValue
GetEnvironmentValue.restype = STRING
GetEnvironmentValue.argtypes = [STRING]
StringInfoToHexString = _lib.StringInfoToHexString
StringInfoToHexString.restype = STRING
StringInfoToHexString.argtypes = [POINTER(StringInfo)]
StringInfoToString = _lib.StringInfoToString
StringInfoToString.restype = STRING
StringInfoToString.argtypes = [POINTER(StringInfo)]
StringToArgv = _lib.StringToArgv
StringToArgv.restype = POINTER(STRING)
StringToArgv.argtypes = [STRING, POINTER(c_int)]
StringToken = _lib.StringToken
StringToken.restype = STRING
StringToken.argtypes = [STRING, POINTER(STRING)]
StringToList = _lib.StringToList
StringToList.restype = POINTER(STRING)
StringToList.argtypes = [STRING]
GetStringInfoPath = _lib.GetStringInfoPath
GetStringInfoPath.restype = STRING
GetStringInfoPath.argtypes = [POINTER(StringInfo)]
CompareStringInfo = _lib.CompareStringInfo
CompareStringInfo.restype = c_int
CompareStringInfo.argtypes = [POINTER(StringInfo), POINTER(StringInfo)]
LocaleCompare = _lib.LocaleCompare
LocaleCompare.restype = c_int
LocaleCompare.argtypes = [STRING, STRING]
LocaleNCompare = _lib.LocaleNCompare
LocaleNCompare.restype = c_int
LocaleNCompare.argtypes = [STRING, STRING, size_t]
ConcatenateString = _lib.ConcatenateString
ConcatenateString.restype = MagickBooleanType
ConcatenateString.argtypes = [POINTER(STRING), STRING]
SubstituteString = _lib.SubstituteString
SubstituteString.restype = MagickBooleanType
SubstituteString.argtypes = [POINTER(STRING), STRING, STRING]
ConcatenateMagickString = _lib.ConcatenateMagickString
ConcatenateMagickString.restype = size_t
ConcatenateMagickString.argtypes = [STRING, STRING, size_t]
CopyMagickString = _lib.CopyMagickString
CopyMagickString.restype = size_t
CopyMagickString.argtypes = [STRING, STRING, size_t]
GetStringInfoLength = _lib.GetStringInfoLength
GetStringInfoLength.restype = size_t
GetStringInfoLength.argtypes = [POINTER(StringInfo)]
FormatMagickSize = _lib.FormatMagickSize
FormatMagickSize.restype = ssize_t
FormatMagickSize.argtypes = [MagickSizeType, MagickBooleanType, STRING]
FormatMagickString = _lib.FormatMagickString
FormatMagickString.restype = ssize_t
FormatMagickString.argtypes = [STRING, size_t, STRING]
FormatMagickStringList = _lib.FormatMagickStringList
FormatMagickStringList.restype = ssize_t
FormatMagickStringList.argtypes = [STRING, size_t, STRING, POINTER(__va_list_tag)]
__time_t = c_long
time_t = __time_t
FormatMagickTime = _lib.FormatMagickTime
FormatMagickTime.restype = ssize_t
FormatMagickTime.argtypes = [time_t, size_t, STRING]
AcquireStringInfo = _lib.AcquireStringInfo
AcquireStringInfo.restype = POINTER(StringInfo)
AcquireStringInfo.argtypes = [size_t]
CloneStringInfo = _lib.CloneStringInfo
CloneStringInfo.restype = POINTER(StringInfo)
CloneStringInfo.argtypes = [POINTER(StringInfo)]
ConfigureFileToStringInfo = _lib.ConfigureFileToStringInfo
ConfigureFileToStringInfo.restype = POINTER(StringInfo)
ConfigureFileToStringInfo.argtypes = [STRING]
DestroyStringInfo = _lib.DestroyStringInfo
DestroyStringInfo.restype = POINTER(StringInfo)
DestroyStringInfo.argtypes = [POINTER(StringInfo)]
FileToStringInfo = _lib.FileToStringInfo
FileToStringInfo.restype = POINTER(StringInfo)
FileToStringInfo.argtypes = [STRING, size_t, POINTER(ExceptionInfo)]
SplitStringInfo = _lib.SplitStringInfo
SplitStringInfo.restype = POINTER(StringInfo)
SplitStringInfo.argtypes = [POINTER(StringInfo), size_t]
StringToStringInfo = _lib.StringToStringInfo
StringToStringInfo.restype = POINTER(StringInfo)
StringToStringInfo.argtypes = [STRING]
GetStringInfoDatum = _lib.GetStringInfoDatum
GetStringInfoDatum.restype = POINTER(c_ubyte)
GetStringInfoDatum.argtypes = [POINTER(StringInfo)]
ConcatenateStringInfo = _lib.ConcatenateStringInfo
ConcatenateStringInfo.restype = None
ConcatenateStringInfo.argtypes = [POINTER(StringInfo), POINTER(StringInfo)]
LocaleLower = _lib.LocaleLower
LocaleLower.restype = None
LocaleLower.argtypes = [STRING]
LocaleUpper = _lib.LocaleUpper
LocaleUpper.restype = None
LocaleUpper.argtypes = [STRING]
PrintStringInfo = _lib.PrintStringInfo
PrintStringInfo.restype = None
PrintStringInfo.argtypes = [POINTER(FILE), STRING, POINTER(StringInfo)]
ResetStringInfo = _lib.ResetStringInfo
ResetStringInfo.restype = None
ResetStringInfo.argtypes = [POINTER(StringInfo)]
SetStringInfo = _lib.SetStringInfo
SetStringInfo.restype = None
SetStringInfo.argtypes = [POINTER(StringInfo), POINTER(StringInfo)]
SetStringInfoDatum = _lib.SetStringInfoDatum
SetStringInfoDatum.restype = None
SetStringInfoDatum.argtypes = [POINTER(StringInfo), POINTER(c_ubyte)]
SetStringInfoLength = _lib.SetStringInfoLength
SetStringInfoLength.restype = None
SetStringInfoLength.argtypes = [POINTER(StringInfo), size_t]
SetStringInfoPath = _lib.SetStringInfoPath
SetStringInfoPath.restype = None
SetStringInfoPath.argtypes = [POINTER(StringInfo), STRING]
StripString = _lib.StripString
StripString.restype = None
StripString.argtypes = [STRING]
class _ThresholdMap(Structure):
    pass
ThresholdMap = _ThresholdMap
AdaptiveThresholdImage = _lib.AdaptiveThresholdImage
AdaptiveThresholdImage.restype = POINTER(Image)
AdaptiveThresholdImage.argtypes = [POINTER(Image), size_t, size_t, ssize_t, POINTER(ExceptionInfo)]
DestroyThresholdMap = _lib.DestroyThresholdMap
DestroyThresholdMap.restype = POINTER(ThresholdMap)
DestroyThresholdMap.argtypes = [POINTER(ThresholdMap)]
GetThresholdMap = _lib.GetThresholdMap
GetThresholdMap.restype = POINTER(ThresholdMap)
GetThresholdMap.argtypes = [STRING, POINTER(ExceptionInfo)]
BilevelImage = _lib.BilevelImage
BilevelImage.restype = MagickBooleanType
BilevelImage.argtypes = [POINTER(Image), c_double]
BilevelImageChannel = _lib.BilevelImageChannel
BilevelImageChannel.restype = MagickBooleanType
BilevelImageChannel.argtypes = [POINTER(Image), ChannelType, c_double]
BlackThresholdImage = _lib.BlackThresholdImage
BlackThresholdImage.restype = MagickBooleanType
BlackThresholdImage.argtypes = [POINTER(Image), STRING]
BlackThresholdImageChannel = _lib.BlackThresholdImageChannel
BlackThresholdImageChannel.restype = MagickBooleanType
BlackThresholdImageChannel.argtypes = [POINTER(Image), ChannelType, STRING, POINTER(ExceptionInfo)]
ClampImage = _lib.ClampImage
ClampImage.restype = MagickBooleanType
ClampImage.argtypes = [POINTER(Image)]
ClampImageChannel = _lib.ClampImageChannel
ClampImageChannel.restype = MagickBooleanType
ClampImageChannel.argtypes = [POINTER(Image), ChannelType]
ListThresholdMaps = _lib.ListThresholdMaps
ListThresholdMaps.restype = MagickBooleanType
ListThresholdMaps.argtypes = [POINTER(FILE), POINTER(ExceptionInfo)]
OrderedDitherImage = _lib.OrderedDitherImage
OrderedDitherImage.restype = MagickBooleanType
OrderedDitherImage.argtypes = [POINTER(Image)]
OrderedDitherImageChannel = _lib.OrderedDitherImageChannel
OrderedDitherImageChannel.restype = MagickBooleanType
OrderedDitherImageChannel.argtypes = [POINTER(Image), ChannelType, POINTER(ExceptionInfo)]
OrderedPosterizeImage = _lib.OrderedPosterizeImage
OrderedPosterizeImage.restype = MagickBooleanType
OrderedPosterizeImage.argtypes = [POINTER(Image), STRING, POINTER(ExceptionInfo)]
OrderedPosterizeImageChannel = _lib.OrderedPosterizeImageChannel
OrderedPosterizeImageChannel.restype = MagickBooleanType
OrderedPosterizeImageChannel.argtypes = [POINTER(Image), ChannelType, STRING, POINTER(ExceptionInfo)]
RandomThresholdImage = _lib.RandomThresholdImage
RandomThresholdImage.restype = MagickBooleanType
RandomThresholdImage.argtypes = [POINTER(Image), STRING, POINTER(ExceptionInfo)]
RandomThresholdImageChannel = _lib.RandomThresholdImageChannel
RandomThresholdImageChannel.restype = MagickBooleanType
RandomThresholdImageChannel.argtypes = [POINTER(Image), ChannelType, STRING, POINTER(ExceptionInfo)]
WhiteThresholdImage = _lib.WhiteThresholdImage
WhiteThresholdImage.restype = MagickBooleanType
WhiteThresholdImage.argtypes = [POINTER(Image), STRING]
WhiteThresholdImageChannel = _lib.WhiteThresholdImageChannel
WhiteThresholdImageChannel.restype = MagickBooleanType
WhiteThresholdImageChannel.argtypes = [POINTER(Image), ChannelType, STRING, POINTER(ExceptionInfo)]

# values for enumeration 'TimerState'
TimerState = c_int # enum
class _Timer(Structure):
    pass
Timer = _Timer
class _TimerInfo(Structure):
    pass
TimerInfo = _TimerInfo
GetElapsedTime = _lib.GetElapsedTime
GetElapsedTime.restype = c_double
GetElapsedTime.argtypes = [POINTER(TimerInfo)]
GetUserTime = _lib.GetUserTime
GetUserTime.restype = c_double
GetUserTime.argtypes = [POINTER(TimerInfo)]
ContinueTimer = _lib.ContinueTimer
ContinueTimer.restype = MagickBooleanType
ContinueTimer.argtypes = [POINTER(TimerInfo)]
AcquireTimerInfo = _lib.AcquireTimerInfo
AcquireTimerInfo.restype = POINTER(TimerInfo)
AcquireTimerInfo.argtypes = []
DestroyTimerInfo = _lib.DestroyTimerInfo
DestroyTimerInfo.restype = POINTER(TimerInfo)
DestroyTimerInfo.argtypes = [POINTER(TimerInfo)]
GetTimerInfo = _lib.GetTimerInfo
GetTimerInfo.restype = None
GetTimerInfo.argtypes = [POINTER(TimerInfo)]
ResetTimer = _lib.ResetTimer
ResetTimer.restype = None
ResetTimer.argtypes = [POINTER(TimerInfo)]
StartTimer = _lib.StartTimer
StartTimer.restype = None
StartTimer.argtypes = [POINTER(TimerInfo), MagickBooleanType]
class _TokenInfo(Structure):
    pass
TokenInfo = _TokenInfo
Tokenizer = _lib.Tokenizer
Tokenizer.restype = c_int
Tokenizer.argtypes = [POINTER(TokenInfo), c_uint, STRING, size_t, STRING, STRING, STRING, STRING, c_char, STRING, POINTER(c_int), STRING]
GlobExpression = _lib.GlobExpression
GlobExpression.restype = MagickBooleanType
GlobExpression.argtypes = [STRING, STRING, MagickBooleanType]
IsGlob = _lib.IsGlob
IsGlob.restype = MagickBooleanType
IsGlob.argtypes = [STRING]
AcquireTokenInfo = _lib.AcquireTokenInfo
AcquireTokenInfo.restype = POINTER(TokenInfo)
AcquireTokenInfo.argtypes = []
DestroyTokenInfo = _lib.DestroyTokenInfo
DestroyTokenInfo.restype = POINTER(TokenInfo)
DestroyTokenInfo.argtypes = [POINTER(TokenInfo)]
GetMagickToken = _lib.GetMagickToken
GetMagickToken.restype = None
GetMagickToken.argtypes = [STRING, POINTER(STRING), STRING]
ChopImage = _lib.ChopImage
ChopImage.restype = POINTER(Image)
ChopImage.argtypes = [POINTER(Image), POINTER(RectangleInfo), POINTER(ExceptionInfo)]
ConsolidateCMYKImages = _lib.ConsolidateCMYKImages
ConsolidateCMYKImages.restype = POINTER(Image)
ConsolidateCMYKImages.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
CropImage = _lib.CropImage
CropImage.restype = POINTER(Image)
CropImage.argtypes = [POINTER(Image), POINTER(RectangleInfo), POINTER(ExceptionInfo)]
ExcerptImage = _lib.ExcerptImage
ExcerptImage.restype = POINTER(Image)
ExcerptImage.argtypes = [POINTER(Image), POINTER(RectangleInfo), POINTER(ExceptionInfo)]
ExtentImage = _lib.ExtentImage
ExtentImage.restype = POINTER(Image)
ExtentImage.argtypes = [POINTER(Image), POINTER(RectangleInfo), POINTER(ExceptionInfo)]
FlipImage = _lib.FlipImage
FlipImage.restype = POINTER(Image)
FlipImage.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
FlopImage = _lib.FlopImage
FlopImage.restype = POINTER(Image)
FlopImage.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
RollImage = _lib.RollImage
RollImage.restype = POINTER(Image)
RollImage.argtypes = [POINTER(Image), ssize_t, ssize_t, POINTER(ExceptionInfo)]
ShaveImage = _lib.ShaveImage
ShaveImage.restype = POINTER(Image)
ShaveImage.argtypes = [POINTER(Image), POINTER(RectangleInfo), POINTER(ExceptionInfo)]
SpliceImage = _lib.SpliceImage
SpliceImage.restype = POINTER(Image)
SpliceImage.argtypes = [POINTER(Image), POINTER(RectangleInfo), POINTER(ExceptionInfo)]
TransposeImage = _lib.TransposeImage
TransposeImage.restype = POINTER(Image)
TransposeImage.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
TransverseImage = _lib.TransverseImage
TransverseImage.restype = POINTER(Image)
TransverseImage.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
TrimImage = _lib.TrimImage
TrimImage.restype = POINTER(Image)
TrimImage.argtypes = [POINTER(Image), POINTER(ExceptionInfo)]
TransformImage = _lib.TransformImage
TransformImage.restype = MagickBooleanType
TransformImage.argtypes = [POINTER(POINTER(Image)), STRING, STRING]
TransformImages = _lib.TransformImages
TransformImages.restype = MagickBooleanType
TransformImages.argtypes = [POINTER(POINTER(Image)), STRING, STRING]

# values for enumeration 'StretchType'
StretchType = c_int # enum

# values for enumeration 'StyleType'
StyleType = c_int # enum
class _TypeInfo(Structure):
    pass
TypeInfo = _TypeInfo
GetTypeList = _lib.GetTypeList
GetTypeList.restype = POINTER(STRING)
GetTypeList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
ListTypeInfo = _lib.ListTypeInfo
ListTypeInfo.restype = MagickBooleanType
ListTypeInfo.argtypes = [POINTER(FILE), POINTER(ExceptionInfo)]
TypeComponentGenesis = _lib.TypeComponentGenesis
TypeComponentGenesis.restype = MagickBooleanType
TypeComponentGenesis.argtypes = []
GetTypeInfo = _lib.GetTypeInfo
GetTypeInfo.restype = POINTER(TypeInfo)
GetTypeInfo.argtypes = [STRING, POINTER(ExceptionInfo)]
GetTypeInfoByFamily = _lib.GetTypeInfoByFamily
GetTypeInfoByFamily.restype = POINTER(TypeInfo)
GetTypeInfoByFamily.argtypes = [STRING, StyleType, StretchType, size_t, POINTER(ExceptionInfo)]
GetTypeInfoList = _lib.GetTypeInfoList
GetTypeInfoList.restype = POINTER(POINTER(TypeInfo))
GetTypeInfoList.argtypes = [STRING, POINTER(size_t), POINTER(ExceptionInfo)]
TypeComponentTerminus = _lib.TypeComponentTerminus
TypeComponentTerminus.restype = None
TypeComponentTerminus.argtypes = []

# values for enumeration 'PathType'
PathType = c_int # enum
Base64Encode = _lib.Base64Encode
Base64Encode.restype = STRING
Base64Encode.argtypes = [POINTER(c_ubyte), size_t, POINTER(size_t)]
GetPathComponents = _lib.GetPathComponents
GetPathComponents.restype = POINTER(STRING)
GetPathComponents.argtypes = [STRING, POINTER(size_t)]
ListFiles = _lib.ListFiles
ListFiles.restype = POINTER(STRING)
ListFiles.argtypes = [STRING, STRING, POINTER(size_t)]
OpenMagickStream = _lib.OpenMagickStream
OpenMagickStream.restype = POINTER(FILE)
OpenMagickStream.argtypes = [STRING, STRING]
SystemCommand = _lib.SystemCommand
SystemCommand.restype = c_int
SystemCommand.argtypes = [MagickBooleanType, MagickBooleanType, STRING, POINTER(ExceptionInfo)]
AcquireUniqueFilename = _lib.AcquireUniqueFilename
AcquireUniqueFilename.restype = MagickBooleanType
AcquireUniqueFilename.argtypes = [STRING]
AcquireUniqueSymbolicLink = _lib.AcquireUniqueSymbolicLink
AcquireUniqueSymbolicLink.restype = MagickBooleanType
AcquireUniqueSymbolicLink.argtypes = [STRING, STRING]
ExpandFilenames = _lib.ExpandFilenames
ExpandFilenames.restype = MagickBooleanType
ExpandFilenames.argtypes = [POINTER(c_int), POINTER(POINTER(STRING))]
GetPathAttributes = _lib.GetPathAttributes
GetPathAttributes.restype = MagickBooleanType
GetPathAttributes.argtypes = [STRING, c_void_p]
GetExecutionPath = _lib.GetExecutionPath
GetExecutionPath.restype = MagickBooleanType
GetExecutionPath.argtypes = [STRING, size_t]
IsMagickTrue = _lib.IsMagickTrue
IsMagickTrue.restype = MagickBooleanType
IsMagickTrue.argtypes = [STRING]
IsPathAccessible = _lib.IsPathAccessible
IsPathAccessible.restype = MagickBooleanType
IsPathAccessible.argtypes = [STRING]
MultilineCensus = _lib.MultilineCensus
MultilineCensus.restype = size_t
MultilineCensus.argtypes = [STRING]
GetMagickPageSize = _lib.GetMagickPageSize
GetMagickPageSize.restype = ssize_t
GetMagickPageSize.argtypes = []
Base64Decode = _lib.Base64Decode
Base64Decode.restype = POINTER(c_ubyte)
Base64Decode.argtypes = [STRING, POINTER(size_t)]
AppendImageFormat = _lib.AppendImageFormat
AppendImageFormat.restype = None
AppendImageFormat.argtypes = [STRING, STRING]
ChopPathComponents = _lib.ChopPathComponents
ChopPathComponents.restype = None
ChopPathComponents.argtypes = [STRING, size_t]
ExpandFilename = _lib.ExpandFilename
ExpandFilename.restype = None
ExpandFilename.argtypes = [STRING]
GetPathComponent = _lib.GetPathComponent
GetPathComponent.restype = None
GetPathComponent.argtypes = [STRING, PathType, STRING]
GetMagickHomeURL = _lib.GetMagickHomeURL
GetMagickHomeURL.restype = STRING
GetMagickHomeURL.argtypes = []
GetMagickCopyright = _lib.GetMagickCopyright
GetMagickCopyright.restype = STRING
GetMagickCopyright.argtypes = []
GetMagickFeatures = _lib.GetMagickFeatures
GetMagickFeatures.restype = STRING
GetMagickFeatures.argtypes = []
GetMagickPackageName = _lib.GetMagickPackageName
GetMagickPackageName.restype = STRING
GetMagickPackageName.argtypes = []
GetMagickQuantumDepth = _lib.GetMagickQuantumDepth
GetMagickQuantumDepth.restype = STRING
GetMagickQuantumDepth.argtypes = [POINTER(size_t)]
GetMagickQuantumRange = _lib.GetMagickQuantumRange
GetMagickQuantumRange.restype = STRING
GetMagickQuantumRange.argtypes = [POINTER(size_t)]
GetMagickReleaseDate = _lib.GetMagickReleaseDate
GetMagickReleaseDate.restype = STRING
GetMagickReleaseDate.argtypes = []
GetMagickVersion = _lib.GetMagickVersion
GetMagickVersion.restype = STRING
GetMagickVersion.argtypes = [POINTER(size_t)]
class _XMLTreeInfo(Structure):
    pass
XMLTreeInfo = _XMLTreeInfo
CanonicalXMLContent = _lib.CanonicalXMLContent
CanonicalXMLContent.restype = STRING
CanonicalXMLContent.argtypes = [STRING, MagickBooleanType]
XMLTreeInfoToXML = _lib.XMLTreeInfoToXML
XMLTreeInfoToXML.restype = STRING
XMLTreeInfoToXML.argtypes = [POINTER(XMLTreeInfo)]
GetXMLTreeAttribute = _lib.GetXMLTreeAttribute
GetXMLTreeAttribute.restype = STRING
GetXMLTreeAttribute.argtypes = [POINTER(XMLTreeInfo), STRING]
GetXMLTreeContent = _lib.GetXMLTreeContent
GetXMLTreeContent.restype = STRING
GetXMLTreeContent.argtypes = [POINTER(XMLTreeInfo)]
GetXMLTreeProcessingInstructions = _lib.GetXMLTreeProcessingInstructions
GetXMLTreeProcessingInstructions.restype = POINTER(STRING)
GetXMLTreeProcessingInstructions.argtypes = [POINTER(XMLTreeInfo), STRING]
GetXMLTreeTag = _lib.GetXMLTreeTag
GetXMLTreeTag.restype = STRING
GetXMLTreeTag.argtypes = [POINTER(XMLTreeInfo)]
GetXMLTreeAttributes = _lib.GetXMLTreeAttributes
GetXMLTreeAttributes.restype = MagickBooleanType
GetXMLTreeAttributes.argtypes = [POINTER(XMLTreeInfo), POINTER(SplayTreeInfo)]
AddChildToXMLTree = _lib.AddChildToXMLTree
AddChildToXMLTree.restype = POINTER(XMLTreeInfo)
AddChildToXMLTree.argtypes = [POINTER(XMLTreeInfo), STRING, size_t]
AddPathToXMLTree = _lib.AddPathToXMLTree
AddPathToXMLTree.restype = POINTER(XMLTreeInfo)
AddPathToXMLTree.argtypes = [POINTER(XMLTreeInfo), STRING, size_t]
DestroyXMLTree = _lib.DestroyXMLTree
DestroyXMLTree.restype = POINTER(XMLTreeInfo)
DestroyXMLTree.argtypes = [POINTER(XMLTreeInfo)]
GetNextXMLTreeTag = _lib.GetNextXMLTreeTag
GetNextXMLTreeTag.restype = POINTER(XMLTreeInfo)
GetNextXMLTreeTag.argtypes = [POINTER(XMLTreeInfo)]
GetXMLTreeChild = _lib.GetXMLTreeChild
GetXMLTreeChild.restype = POINTER(XMLTreeInfo)
GetXMLTreeChild.argtypes = [POINTER(XMLTreeInfo), STRING]
GetXMLTreeOrdered = _lib.GetXMLTreeOrdered
GetXMLTreeOrdered.restype = POINTER(XMLTreeInfo)
GetXMLTreeOrdered.argtypes = [POINTER(XMLTreeInfo)]
GetXMLTreePath = _lib.GetXMLTreePath
GetXMLTreePath.restype = POINTER(XMLTreeInfo)
GetXMLTreePath.argtypes = [POINTER(XMLTreeInfo), STRING]
GetXMLTreeSibling = _lib.GetXMLTreeSibling
GetXMLTreeSibling.restype = POINTER(XMLTreeInfo)
GetXMLTreeSibling.argtypes = [POINTER(XMLTreeInfo)]
InsertTagIntoXMLTree = _lib.InsertTagIntoXMLTree
InsertTagIntoXMLTree.restype = POINTER(XMLTreeInfo)
InsertTagIntoXMLTree.argtypes = [POINTER(XMLTreeInfo), POINTER(XMLTreeInfo), size_t]
NewXMLTree = _lib.NewXMLTree
NewXMLTree.restype = POINTER(XMLTreeInfo)
NewXMLTree.argtypes = [STRING, POINTER(ExceptionInfo)]
NewXMLTreeTag = _lib.NewXMLTreeTag
NewXMLTreeTag.restype = POINTER(XMLTreeInfo)
NewXMLTreeTag.argtypes = [STRING]
PruneTagFromXMLTree = _lib.PruneTagFromXMLTree
PruneTagFromXMLTree.restype = POINTER(XMLTreeInfo)
PruneTagFromXMLTree.argtypes = [POINTER(XMLTreeInfo)]
SetXMLTreeAttribute = _lib.SetXMLTreeAttribute
SetXMLTreeAttribute.restype = POINTER(XMLTreeInfo)
SetXMLTreeAttribute.argtypes = [POINTER(XMLTreeInfo), STRING, STRING]
SetXMLTreeContent = _lib.SetXMLTreeContent
SetXMLTreeContent.restype = POINTER(XMLTreeInfo)
SetXMLTreeContent.argtypes = [POINTER(XMLTreeInfo), STRING]
class _XImportInfo(Structure):
    pass
XImportInfo = _XImportInfo
XImportImage = _lib.XImportImage
XImportImage.restype = POINTER(Image)
XImportImage.argtypes = [POINTER(ImageInfo), POINTER(XImportInfo)]
XGetImportInfo = _lib.XGetImportInfo
XGetImportInfo.restype = None
XGetImportInfo.argtypes = [POINTER(XImportInfo)]
class _MagickWand(Structure):
    pass
MagickWand = _MagickWand
MagickGetException = _lib.MagickGetException
MagickGetException.restype = STRING
MagickGetException.argtypes = [POINTER(MagickWand), POINTER(ExceptionType)]
MagickGetExceptionType = _lib.MagickGetExceptionType
MagickGetExceptionType.restype = ExceptionType
MagickGetExceptionType.argtypes = [POINTER(MagickWand)]
IsMagickWand = _lib.IsMagickWand
IsMagickWand.restype = MagickBooleanType
IsMagickWand.argtypes = [POINTER(MagickWand)]
MagickClearException = _lib.MagickClearException
MagickClearException.restype = MagickBooleanType
MagickClearException.argtypes = [POINTER(MagickWand)]
MagickSetIteratorIndex = _lib.MagickSetIteratorIndex
MagickSetIteratorIndex.restype = MagickBooleanType
MagickSetIteratorIndex.argtypes = [POINTER(MagickWand), ssize_t]
CloneMagickWand = _lib.CloneMagickWand
CloneMagickWand.restype = POINTER(MagickWand)
CloneMagickWand.argtypes = [POINTER(MagickWand)]
DestroyMagickWand = _lib.DestroyMagickWand
DestroyMagickWand.restype = POINTER(MagickWand)
DestroyMagickWand.argtypes = [POINTER(MagickWand)]
NewMagickWand = _lib.NewMagickWand
NewMagickWand.restype = POINTER(MagickWand)
NewMagickWand.argtypes = []
NewMagickWandFromImage = _lib.NewMagickWandFromImage
NewMagickWandFromImage.restype = POINTER(MagickWand)
NewMagickWandFromImage.argtypes = [POINTER(Image)]
MagickGetIteratorIndex = _lib.MagickGetIteratorIndex
MagickGetIteratorIndex.restype = ssize_t
MagickGetIteratorIndex.argtypes = [POINTER(MagickWand)]
ClearMagickWand = _lib.ClearMagickWand
ClearMagickWand.restype = None
ClearMagickWand.argtypes = [POINTER(MagickWand)]
MagickWandGenesis = _lib.MagickWandGenesis
MagickWandGenesis.restype = None
MagickWandGenesis.argtypes = []
MagickWandTerminus = _lib.MagickWandTerminus
MagickWandTerminus.restype = None
MagickWandTerminus.argtypes = []
MagickRelinquishMemory = _lib.MagickRelinquishMemory
MagickRelinquishMemory.restype = c_void_p
MagickRelinquishMemory.argtypes = [c_void_p]
MagickResetIterator = _lib.MagickResetIterator
MagickResetIterator.restype = None
MagickResetIterator.argtypes = [POINTER(MagickWand)]
MagickSetFirstIterator = _lib.MagickSetFirstIterator
MagickSetFirstIterator.restype = None
MagickSetFirstIterator.argtypes = [POINTER(MagickWand)]
MagickSetLastIterator = _lib.MagickSetLastIterator
MagickSetLastIterator.restype = None
MagickSetLastIterator.argtypes = [POINTER(MagickWand)]
AnimateImageCommand = _lib.AnimateImageCommand
AnimateImageCommand.restype = MagickBooleanType
AnimateImageCommand.argtypes = [POINTER(ImageInfo), c_int, POINTER(STRING), POINTER(STRING), POINTER(ExceptionInfo)]
CompareImageCommand = _lib.CompareImageCommand
CompareImageCommand.restype = MagickBooleanType
CompareImageCommand.argtypes = [POINTER(ImageInfo), c_int, POINTER(STRING), POINTER(STRING), POINTER(ExceptionInfo)]
CompositeImageCommand = _lib.CompositeImageCommand
CompositeImageCommand.restype = MagickBooleanType
CompositeImageCommand.argtypes = [POINTER(ImageInfo), c_int, POINTER(STRING), POINTER(STRING), POINTER(ExceptionInfo)]
ConjureImageCommand = _lib.ConjureImageCommand
ConjureImageCommand.restype = MagickBooleanType
ConjureImageCommand.argtypes = [POINTER(ImageInfo), c_int, POINTER(STRING), POINTER(STRING), POINTER(ExceptionInfo)]
ConvertImageCommand = _lib.ConvertImageCommand
ConvertImageCommand.restype = MagickBooleanType
ConvertImageCommand.argtypes = [POINTER(ImageInfo), c_int, POINTER(STRING), POINTER(STRING), POINTER(ExceptionInfo)]
class _DrawingWand(Structure):
    pass
DrawContext = POINTER(_DrawingWand)
DrawingWand = _DrawingWand
DrawGetFillAlpha = _lib.DrawGetFillAlpha
DrawGetFillAlpha.restype = c_double
DrawGetFillAlpha.argtypes = [POINTER(DrawingWand)]
DrawGetStrokeAlpha = _lib.DrawGetStrokeAlpha
DrawGetStrokeAlpha.restype = c_double
DrawGetStrokeAlpha.argtypes = [POINTER(DrawingWand)]
DrawPeekGraphicWand = _lib.DrawPeekGraphicWand
DrawPeekGraphicWand.restype = POINTER(DrawInfo)
DrawPeekGraphicWand.argtypes = [POINTER(DrawingWand)]
MagickDescribeImage = _lib.MagickDescribeImage
MagickDescribeImage.restype = STRING
MagickDescribeImage.argtypes = [POINTER(MagickWand)]
MagickGetImageAttribute = _lib.MagickGetImageAttribute
MagickGetImageAttribute.restype = STRING
MagickGetImageAttribute.argtypes = [POINTER(MagickWand), STRING]
class _PixelIterator(Structure):
    pass
PixelIterator = _PixelIterator
PixelIteratorGetException = _lib.PixelIteratorGetException
PixelIteratorGetException.restype = STRING
PixelIteratorGetException.argtypes = [POINTER(PixelIterator), POINTER(ExceptionType)]
MagickGetImageIndex = _lib.MagickGetImageIndex
MagickGetImageIndex.restype = ssize_t
MagickGetImageIndex.argtypes = [POINTER(MagickWand)]
MagickClipPathImage = _lib.MagickClipPathImage
MagickClipPathImage.restype = MagickBooleanType
MagickClipPathImage.argtypes = [POINTER(MagickWand), STRING, MagickBooleanType]
class _PixelWand(Structure):
    pass
PixelWand = _PixelWand
MagickColorFloodfillImage = _lib.MagickColorFloodfillImage
MagickColorFloodfillImage.restype = MagickBooleanType
MagickColorFloodfillImage.argtypes = [POINTER(MagickWand), POINTER(PixelWand), c_double, POINTER(PixelWand), ssize_t, ssize_t]
MagickGetImageChannelExtrema = _lib.MagickGetImageChannelExtrema
MagickGetImageChannelExtrema.restype = MagickBooleanType
MagickGetImageChannelExtrema.argtypes = [POINTER(MagickWand), ChannelType, POINTER(size_t), POINTER(size_t)]
MagickGetImageExtrema = _lib.MagickGetImageExtrema
MagickGetImageExtrema.restype = MagickBooleanType
MagickGetImageExtrema.argtypes = [POINTER(MagickWand), POINTER(size_t), POINTER(size_t)]
MagickGetImageMatte = _lib.MagickGetImageMatte
MagickGetImageMatte.restype = MagickBooleanType
MagickGetImageMatte.argtypes = [POINTER(MagickWand)]
MagickGetImagePixels = _lib.MagickGetImagePixels
MagickGetImagePixels.restype = MagickBooleanType
MagickGetImagePixels.argtypes = [POINTER(MagickWand), ssize_t, ssize_t, size_t, size_t, STRING, StorageType, c_void_p]
MagickMapImage = _lib.MagickMapImage
MagickMapImage.restype = MagickBooleanType
MagickMapImage.argtypes = [POINTER(MagickWand), POINTER(MagickWand), MagickBooleanType]
MagickMatteFloodfillImage = _lib.MagickMatteFloodfillImage
MagickMatteFloodfillImage.restype = MagickBooleanType
MagickMatteFloodfillImage.argtypes = [POINTER(MagickWand), c_double, c_double, POINTER(PixelWand), ssize_t, ssize_t]
MagickOpaqueImage = _lib.MagickOpaqueImage
MagickOpaqueImage.restype = MagickBooleanType
MagickOpaqueImage.argtypes = [POINTER(MagickWand), POINTER(PixelWand), POINTER(PixelWand), c_double]
MagickPaintFloodfillImage = _lib.MagickPaintFloodfillImage
MagickPaintFloodfillImage.restype = MagickBooleanType
MagickPaintFloodfillImage.argtypes = [POINTER(MagickWand), ChannelType, POINTER(PixelWand), c_double, POINTER(PixelWand), ssize_t, ssize_t]
MagickPaintOpaqueImage = _lib.MagickPaintOpaqueImage
MagickPaintOpaqueImage.restype = MagickBooleanType
MagickPaintOpaqueImage.argtypes = [POINTER(MagickWand), POINTER(PixelWand), POINTER(PixelWand), c_double]
MagickPaintOpaqueImageChannel = _lib.MagickPaintOpaqueImageChannel
MagickPaintOpaqueImageChannel.restype = MagickBooleanType
MagickPaintOpaqueImageChannel.argtypes = [POINTER(MagickWand), ChannelType, POINTER(PixelWand), POINTER(PixelWand), c_double]
MagickPaintTransparentImage = _lib.MagickPaintTransparentImage
MagickPaintTransparentImage.restype = MagickBooleanType
MagickPaintTransparentImage.argtypes = [POINTER(MagickWand), POINTER(PixelWand), c_double, c_double]
MagickRecolorImage = _lib.MagickRecolorImage
MagickRecolorImage.restype = MagickBooleanType
MagickRecolorImage.argtypes = [POINTER(MagickWand), size_t, POINTER(c_double)]
MagickSetImageAttribute = _lib.MagickSetImageAttribute
MagickSetImageAttribute.restype = MagickBooleanType
MagickSetImageAttribute.argtypes = [POINTER(MagickWand), STRING, STRING]
MagickSetImageIndex = _lib.MagickSetImageIndex
MagickSetImageIndex.restype = MagickBooleanType
MagickSetImageIndex.argtypes = [POINTER(MagickWand), ssize_t]
MagickSetImageOption = _lib.MagickSetImageOption
MagickSetImageOption.restype = MagickBooleanType
MagickSetImageOption.argtypes = [POINTER(MagickWand), STRING, STRING, STRING]
MagickSetImagePixels = _lib.MagickSetImagePixels
MagickSetImagePixels.restype = MagickBooleanType
MagickSetImagePixels.argtypes = [POINTER(MagickWand), ssize_t, ssize_t, size_t, size_t, STRING, StorageType, c_void_p]
MagickTransparentImage = _lib.MagickTransparentImage
MagickTransparentImage.restype = MagickBooleanType
MagickTransparentImage.argtypes = [POINTER(MagickWand), POINTER(PixelWand), c_double, c_double]
MagickAverageImages = _lib.MagickAverageImages
MagickAverageImages.restype = POINTER(MagickWand)
MagickAverageImages.argtypes = [POINTER(MagickWand)]
MagickFlattenImages = _lib.MagickFlattenImages
MagickFlattenImages.restype = POINTER(MagickWand)
MagickFlattenImages.argtypes = [POINTER(MagickWand)]
MagickMaximumImages = _lib.MagickMaximumImages
MagickMaximumImages.restype = POINTER(MagickWand)
MagickMaximumImages.argtypes = [POINTER(MagickWand)]
MagickMinimumImages = _lib.MagickMinimumImages
MagickMinimumImages.restype = POINTER(MagickWand)
MagickMinimumImages.argtypes = [POINTER(MagickWand)]
MagickMosaicImages = _lib.MagickMosaicImages
MagickMosaicImages.restype = POINTER(MagickWand)
MagickMosaicImages.argtypes = [POINTER(MagickWand)]
MagickRegionOfInterestImage = _lib.MagickRegionOfInterestImage
MagickRegionOfInterestImage.restype = POINTER(MagickWand)
MagickRegionOfInterestImage.argtypes = [POINTER(MagickWand), size_t, size_t, ssize_t, ssize_t]
MagickGetImageSize = _lib.MagickGetImageSize
MagickGetImageSize.restype = MagickSizeType
MagickGetImageSize.argtypes = [POINTER(MagickWand)]
PixelGetNextRow = _lib.PixelGetNextRow
PixelGetNextRow.restype = POINTER(POINTER(PixelWand))
PixelGetNextRow.argtypes = [POINTER(PixelIterator)]
MagickWriteImageBlob = _lib.MagickWriteImageBlob
MagickWriteImageBlob.restype = POINTER(c_ubyte)
MagickWriteImageBlob.argtypes = [POINTER(MagickWand), POINTER(size_t)]
DrawPopGraphicContext = _lib.DrawPopGraphicContext
DrawPopGraphicContext.restype = None
DrawPopGraphicContext.argtypes = [POINTER(DrawingWand)]
DrawPushGraphicContext = _lib.DrawPushGraphicContext
DrawPushGraphicContext.restype = None
DrawPushGraphicContext.argtypes = [POINTER(DrawingWand)]
DrawSetFillAlpha = _lib.DrawSetFillAlpha
DrawSetFillAlpha.restype = None
DrawSetFillAlpha.argtypes = [POINTER(DrawingWand), c_double]
DrawSetStrokeAlpha = _lib.DrawSetStrokeAlpha
DrawSetStrokeAlpha.restype = None
DrawSetStrokeAlpha.argtypes = [POINTER(DrawingWand), c_double]
DisplayImageCommand = _lib.DisplayImageCommand
DisplayImageCommand.restype = MagickBooleanType
DisplayImageCommand.argtypes = [POINTER(ImageInfo), c_int, POINTER(STRING), POINTER(STRING), POINTER(ExceptionInfo)]
DrawGetTextAlignment = _lib.DrawGetTextAlignment
DrawGetTextAlignment.restype = AlignType
DrawGetTextAlignment.argtypes = [POINTER(DrawingWand)]
DrawGetClipPath = _lib.DrawGetClipPath
DrawGetClipPath.restype = STRING
DrawGetClipPath.argtypes = [POINTER(DrawingWand)]
DrawGetException = _lib.DrawGetException
DrawGetException.restype = STRING
DrawGetException.argtypes = [POINTER(DrawingWand), POINTER(ExceptionType)]
DrawGetFont = _lib.DrawGetFont
DrawGetFont.restype = STRING
DrawGetFont.argtypes = [POINTER(DrawingWand)]
DrawGetFontFamily = _lib.DrawGetFontFamily
DrawGetFontFamily.restype = STRING
DrawGetFontFamily.argtypes = [POINTER(DrawingWand)]
DrawGetTextEncoding = _lib.DrawGetTextEncoding
DrawGetTextEncoding.restype = STRING
DrawGetTextEncoding.argtypes = [POINTER(DrawingWand)]
DrawGetVectorGraphics = _lib.DrawGetVectorGraphics
DrawGetVectorGraphics.restype = STRING
DrawGetVectorGraphics.argtypes = [POINTER(DrawingWand)]
DrawGetClipUnits = _lib.DrawGetClipUnits
DrawGetClipUnits.restype = ClipPathUnits
DrawGetClipUnits.argtypes = [POINTER(DrawingWand)]
DrawGetTextDecoration = _lib.DrawGetTextDecoration
DrawGetTextDecoration.restype = DecorationType
DrawGetTextDecoration.argtypes = [POINTER(DrawingWand)]
DrawGetFillOpacity = _lib.DrawGetFillOpacity
DrawGetFillOpacity.restype = c_double
DrawGetFillOpacity.argtypes = [POINTER(DrawingWand)]
DrawGetFontSize = _lib.DrawGetFontSize
DrawGetFontSize.restype = c_double
DrawGetFontSize.argtypes = [POINTER(DrawingWand)]
DrawGetOpacity = _lib.DrawGetOpacity
DrawGetOpacity.restype = c_double
DrawGetOpacity.argtypes = [POINTER(DrawingWand)]
DrawGetStrokeDashArray = _lib.DrawGetStrokeDashArray
DrawGetStrokeDashArray.restype = POINTER(c_double)
DrawGetStrokeDashArray.argtypes = [POINTER(DrawingWand), POINTER(size_t)]
DrawGetStrokeDashOffset = _lib.DrawGetStrokeDashOffset
DrawGetStrokeDashOffset.restype = c_double
DrawGetStrokeDashOffset.argtypes = [POINTER(DrawingWand)]
DrawGetStrokeOpacity = _lib.DrawGetStrokeOpacity
DrawGetStrokeOpacity.restype = c_double
DrawGetStrokeOpacity.argtypes = [POINTER(DrawingWand)]
DrawGetStrokeWidth = _lib.DrawGetStrokeWidth
DrawGetStrokeWidth.restype = c_double
DrawGetStrokeWidth.argtypes = [POINTER(DrawingWand)]
DrawGetTextKerning = _lib.DrawGetTextKerning
DrawGetTextKerning.restype = c_double
DrawGetTextKerning.argtypes = [POINTER(DrawingWand)]
DrawGetTextInterlineSpacing = _lib.DrawGetTextInterlineSpacing
DrawGetTextInterlineSpacing.restype = c_double
DrawGetTextInterlineSpacing.argtypes = [POINTER(DrawingWand)]
DrawGetTextInterwordSpacing = _lib.DrawGetTextInterwordSpacing
DrawGetTextInterwordSpacing.restype = c_double
DrawGetTextInterwordSpacing.argtypes = [POINTER(DrawingWand)]
PeekDrawingWand = _lib.PeekDrawingWand
PeekDrawingWand.restype = POINTER(DrawInfo)
PeekDrawingWand.argtypes = [POINTER(DrawingWand)]
CloneDrawingWand = _lib.CloneDrawingWand
CloneDrawingWand.restype = POINTER(DrawingWand)
CloneDrawingWand.argtypes = [POINTER(DrawingWand)]
DestroyDrawingWand = _lib.DestroyDrawingWand
DestroyDrawingWand.restype = POINTER(DrawingWand)
DestroyDrawingWand.argtypes = [POINTER(DrawingWand)]
DrawAllocateWand = _lib.DrawAllocateWand
DrawAllocateWand.restype = POINTER(DrawingWand)
DrawAllocateWand.argtypes = [POINTER(DrawInfo), POINTER(Image)]
NewDrawingWand = _lib.NewDrawingWand
NewDrawingWand.restype = POINTER(DrawingWand)
NewDrawingWand.argtypes = []
DrawGetExceptionType = _lib.DrawGetExceptionType
DrawGetExceptionType.restype = ExceptionType
DrawGetExceptionType.argtypes = [POINTER(DrawingWand)]
DrawGetClipRule = _lib.DrawGetClipRule
DrawGetClipRule.restype = FillRule
DrawGetClipRule.argtypes = [POINTER(DrawingWand)]
DrawGetFillRule = _lib.DrawGetFillRule
DrawGetFillRule.restype = FillRule
DrawGetFillRule.argtypes = [POINTER(DrawingWand)]
DrawGetGravity = _lib.DrawGetGravity
DrawGetGravity.restype = GravityType
DrawGetGravity.argtypes = [POINTER(DrawingWand)]
DrawGetStrokeLineCap = _lib.DrawGetStrokeLineCap
DrawGetStrokeLineCap.restype = LineCap
DrawGetStrokeLineCap.argtypes = [POINTER(DrawingWand)]
DrawGetStrokeLineJoin = _lib.DrawGetStrokeLineJoin
DrawGetStrokeLineJoin.restype = LineJoin
DrawGetStrokeLineJoin.argtypes = [POINTER(DrawingWand)]
DrawClearException = _lib.DrawClearException
DrawClearException.restype = MagickBooleanType
DrawClearException.argtypes = [POINTER(DrawingWand)]
DrawComposite = _lib.DrawComposite
DrawComposite.restype = MagickBooleanType
DrawComposite.argtypes = [POINTER(DrawingWand), CompositeOperator, c_double, c_double, c_double, c_double, POINTER(MagickWand)]
DrawGetStrokeAntialias = _lib.DrawGetStrokeAntialias
DrawGetStrokeAntialias.restype = MagickBooleanType
DrawGetStrokeAntialias.argtypes = [POINTER(DrawingWand)]
DrawGetTextAntialias = _lib.DrawGetTextAntialias
DrawGetTextAntialias.restype = MagickBooleanType
DrawGetTextAntialias.argtypes = [POINTER(DrawingWand)]
DrawPopPattern = _lib.DrawPopPattern
DrawPopPattern.restype = MagickBooleanType
DrawPopPattern.argtypes = [POINTER(DrawingWand)]
DrawPushPattern = _lib.DrawPushPattern
DrawPushPattern.restype = MagickBooleanType
DrawPushPattern.argtypes = [POINTER(DrawingWand), STRING, c_double, c_double, c_double, c_double]
DrawRender = _lib.DrawRender
DrawRender.restype = MagickBooleanType
DrawRender.argtypes = [POINTER(DrawingWand)]
DrawSetClipPath = _lib.DrawSetClipPath
DrawSetClipPath.restype = MagickBooleanType
DrawSetClipPath.argtypes = [POINTER(DrawingWand), STRING]
DrawSetFillPatternURL = _lib.DrawSetFillPatternURL
DrawSetFillPatternURL.restype = MagickBooleanType
DrawSetFillPatternURL.argtypes = [POINTER(DrawingWand), STRING]
DrawSetFont = _lib.DrawSetFont
DrawSetFont.restype = MagickBooleanType
DrawSetFont.argtypes = [POINTER(DrawingWand), STRING]
DrawSetFontFamily = _lib.DrawSetFontFamily
DrawSetFontFamily.restype = MagickBooleanType
DrawSetFontFamily.argtypes = [POINTER(DrawingWand), STRING]
DrawSetStrokeDashArray = _lib.DrawSetStrokeDashArray
DrawSetStrokeDashArray.restype = MagickBooleanType
DrawSetStrokeDashArray.argtypes = [POINTER(DrawingWand), size_t, POINTER(c_double)]
DrawSetStrokePatternURL = _lib.DrawSetStrokePatternURL
DrawSetStrokePatternURL.restype = MagickBooleanType
DrawSetStrokePatternURL.argtypes = [POINTER(DrawingWand), STRING]
DrawSetVectorGraphics = _lib.DrawSetVectorGraphics
DrawSetVectorGraphics.restype = MagickBooleanType
DrawSetVectorGraphics.argtypes = [POINTER(DrawingWand), STRING]
IsDrawingWand = _lib.IsDrawingWand
IsDrawingWand.restype = MagickBooleanType
IsDrawingWand.argtypes = [POINTER(DrawingWand)]
PopDrawingWand = _lib.PopDrawingWand
PopDrawingWand.restype = MagickBooleanType
PopDrawingWand.argtypes = [POINTER(DrawingWand)]
PushDrawingWand = _lib.PushDrawingWand
PushDrawingWand.restype = MagickBooleanType
PushDrawingWand.argtypes = [POINTER(DrawingWand)]
DrawGetFontStretch = _lib.DrawGetFontStretch
DrawGetFontStretch.restype = StretchType
DrawGetFontStretch.argtypes = [POINTER(DrawingWand)]
DrawGetFontStyle = _lib.DrawGetFontStyle
DrawGetFontStyle.restype = StyleType
DrawGetFontStyle.argtypes = [POINTER(DrawingWand)]
DrawGetFontWeight = _lib.DrawGetFontWeight
DrawGetFontWeight.restype = size_t
DrawGetFontWeight.argtypes = [POINTER(DrawingWand)]
DrawGetStrokeMiterLimit = _lib.DrawGetStrokeMiterLimit
DrawGetStrokeMiterLimit.restype = size_t
DrawGetStrokeMiterLimit.argtypes = [POINTER(DrawingWand)]
ClearDrawingWand = _lib.ClearDrawingWand
ClearDrawingWand.restype = None
ClearDrawingWand.argtypes = [POINTER(DrawingWand)]
DrawAffine = _lib.DrawAffine
DrawAffine.restype = None
DrawAffine.argtypes = [POINTER(DrawingWand), POINTER(AffineMatrix)]
DrawAnnotation = _lib.DrawAnnotation
DrawAnnotation.restype = None
DrawAnnotation.argtypes = [POINTER(DrawingWand), c_double, c_double, POINTER(c_ubyte)]
DrawArc = _lib.DrawArc
DrawArc.restype = None
DrawArc.argtypes = [POINTER(DrawingWand), c_double, c_double, c_double, c_double, c_double, c_double]
DrawBezier = _lib.DrawBezier
DrawBezier.restype = None
DrawBezier.argtypes = [POINTER(DrawingWand), size_t, POINTER(PointInfo)]
DrawGetBorderColor = _lib.DrawGetBorderColor
DrawGetBorderColor.restype = None
DrawGetBorderColor.argtypes = [POINTER(DrawingWand), POINTER(PixelWand)]
DrawCircle = _lib.DrawCircle
DrawCircle.restype = None
DrawCircle.argtypes = [POINTER(DrawingWand), c_double, c_double, c_double, c_double]
DrawColor = _lib.DrawColor
DrawColor.restype = None
DrawColor.argtypes = [POINTER(DrawingWand), c_double, c_double, PaintMethod]
DrawComment = _lib.DrawComment
DrawComment.restype = None
DrawComment.argtypes = [POINTER(DrawingWand), STRING]
DrawEllipse = _lib.DrawEllipse
DrawEllipse.restype = None
DrawEllipse.argtypes = [POINTER(DrawingWand), c_double, c_double, c_double, c_double, c_double, c_double]
DrawGetFillColor = _lib.DrawGetFillColor
DrawGetFillColor.restype = None
DrawGetFillColor.argtypes = [POINTER(DrawingWand), POINTER(PixelWand)]
DrawGetStrokeColor = _lib.DrawGetStrokeColor
DrawGetStrokeColor.restype = None
DrawGetStrokeColor.argtypes = [POINTER(DrawingWand), POINTER(PixelWand)]
DrawSetTextKerning = _lib.DrawSetTextKerning
DrawSetTextKerning.restype = None
DrawSetTextKerning.argtypes = [POINTER(DrawingWand), c_double]
DrawSetTextInterlineSpacing = _lib.DrawSetTextInterlineSpacing
DrawSetTextInterlineSpacing.restype = None
DrawSetTextInterlineSpacing.argtypes = [POINTER(DrawingWand), c_double]
DrawSetTextInterwordSpacing = _lib.DrawSetTextInterwordSpacing
DrawSetTextInterwordSpacing.restype = None
DrawSetTextInterwordSpacing.argtypes = [POINTER(DrawingWand), c_double]
DrawGetTextUnderColor = _lib.DrawGetTextUnderColor
DrawGetTextUnderColor.restype = None
DrawGetTextUnderColor.argtypes = [POINTER(DrawingWand), POINTER(PixelWand)]
DrawLine = _lib.DrawLine
DrawLine.restype = None
DrawLine.argtypes = [POINTER(DrawingWand), c_double, c_double, c_double, c_double]
DrawMatte = _lib.DrawMatte
DrawMatte.restype = None
DrawMatte.argtypes = [POINTER(DrawingWand), c_double, c_double, PaintMethod]
DrawPathClose = _lib.DrawPathClose
DrawPathClose.restype = None
DrawPathClose.argtypes = [POINTER(DrawingWand)]
DrawPathCurveToAbsolute = _lib.DrawPathCurveToAbsolute
DrawPathCurveToAbsolute.restype = None
DrawPathCurveToAbsolute.argtypes = [POINTER(DrawingWand), c_double, c_double, c_double, c_double, c_double, c_double]
DrawPathCurveToRelative = _lib.DrawPathCurveToRelative
DrawPathCurveToRelative.restype = None
DrawPathCurveToRelative.argtypes = [POINTER(DrawingWand), c_double, c_double, c_double, c_double, c_double, c_double]
DrawPathCurveToQuadraticBezierAbsolute = _lib.DrawPathCurveToQuadraticBezierAbsolute
DrawPathCurveToQuadraticBezierAbsolute.restype = None
DrawPathCurveToQuadraticBezierAbsolute.argtypes = [POINTER(DrawingWand), c_double, c_double, c_double, c_double]
DrawPathCurveToQuadraticBezierRelative = _lib.DrawPathCurveToQuadraticBezierRelative
DrawPathCurveToQuadraticBezierRelative.restype = None
DrawPathCurveToQuadraticBezierRelative.argtypes = [POINTER(DrawingWand), c_double, c_double, c_double, c_double]
DrawPathCurveToQuadraticBezierSmoothAbsolute = _lib.DrawPathCurveToQuadraticBezierSmoothAbsolute
DrawPathCurveToQuadraticBezierSmoothAbsolute.restype = None
DrawPathCurveToQuadraticBezierSmoothAbsolute.argtypes = [POINTER(DrawingWand), c_double, c_double]
DrawPathCurveToQuadraticBezierSmoothRelative = _lib.DrawPathCurveToQuadraticBezierSmoothRelative
DrawPathCurveToQuadraticBezierSmoothRelative.restype = None
DrawPathCurveToQuadraticBezierSmoothRelative.argtypes = [POINTER(DrawingWand), c_double, c_double]
DrawPathCurveToSmoothAbsolute = _lib.DrawPathCurveToSmoothAbsolute
DrawPathCurveToSmoothAbsolute.restype = None
DrawPathCurveToSmoothAbsolute.argtypes = [POINTER(DrawingWand), c_double, c_double, c_double, c_double]
DrawPathCurveToSmoothRelative = _lib.DrawPathCurveToSmoothRelative
DrawPathCurveToSmoothRelative.restype = None
DrawPathCurveToSmoothRelative.argtypes = [POINTER(DrawingWand), c_double, c_double, c_double, c_double]
DrawPathEllipticArcAbsolute = _lib.DrawPathEllipticArcAbsolute
DrawPathEllipticArcAbsolute.restype = None
DrawPathEllipticArcAbsolute.argtypes = [POINTER(DrawingWand), c_double, c_double, c_double, MagickBooleanType, MagickBooleanType, c_double, c_double]
DrawPathEllipticArcRelative = _lib.DrawPathEllipticArcRelative
DrawPathEllipticArcRelative.restype = None
DrawPathEllipticArcRelative.argtypes = [POINTER(DrawingWand), c_double, c_double, c_double, MagickBooleanType, MagickBooleanType, c_double, c_double]
DrawPathFinish = _lib.DrawPathFinish
DrawPathFinish.restype = None
DrawPathFinish.argtypes = [POINTER(DrawingWand)]
DrawPathLineToAbsolute = _lib.DrawPathLineToAbsolute
DrawPathLineToAbsolute.restype = None
DrawPathLineToAbsolute.argtypes = [POINTER(DrawingWand), c_double, c_double]
DrawPathLineToRelative = _lib.DrawPathLineToRelative
DrawPathLineToRelative.restype = None
DrawPathLineToRelative.argtypes = [POINTER(DrawingWand), c_double, c_double]
DrawPathLineToHorizontalAbsolute = _lib.DrawPathLineToHorizontalAbsolute
DrawPathLineToHorizontalAbsolute.restype = None
DrawPathLineToHorizontalAbsolute.argtypes = [POINTER(DrawingWand), c_double]
DrawPathLineToHorizontalRelative = _lib.DrawPathLineToHorizontalRelative
DrawPathLineToHorizontalRelative.restype = None
DrawPathLineToHorizontalRelative.argtypes = [POINTER(DrawingWand), c_double]
DrawPathLineToVerticalAbsolute = _lib.DrawPathLineToVerticalAbsolute
DrawPathLineToVerticalAbsolute.restype = None
DrawPathLineToVerticalAbsolute.argtypes = [POINTER(DrawingWand), c_double]
DrawPathLineToVerticalRelative = _lib.DrawPathLineToVerticalRelative
DrawPathLineToVerticalRelative.restype = None
DrawPathLineToVerticalRelative.argtypes = [POINTER(DrawingWand), c_double]
DrawPathMoveToAbsolute = _lib.DrawPathMoveToAbsolute
DrawPathMoveToAbsolute.restype = None
DrawPathMoveToAbsolute.argtypes = [POINTER(DrawingWand), c_double, c_double]
DrawPathMoveToRelative = _lib.DrawPathMoveToRelative
DrawPathMoveToRelative.restype = None
DrawPathMoveToRelative.argtypes = [POINTER(DrawingWand), c_double, c_double]
DrawPathStart = _lib.DrawPathStart
DrawPathStart.restype = None
DrawPathStart.argtypes = [POINTER(DrawingWand)]
DrawPoint = _lib.DrawPoint
DrawPoint.restype = None
DrawPoint.argtypes = [POINTER(DrawingWand), c_double, c_double]
DrawPolygon = _lib.DrawPolygon
DrawPolygon.restype = None
DrawPolygon.argtypes = [POINTER(DrawingWand), size_t, POINTER(PointInfo)]
DrawPolyline = _lib.DrawPolyline
DrawPolyline.restype = None
DrawPolyline.argtypes = [POINTER(DrawingWand), size_t, POINTER(PointInfo)]
DrawPopClipPath = _lib.DrawPopClipPath
DrawPopClipPath.restype = None
DrawPopClipPath.argtypes = [POINTER(DrawingWand)]
DrawPopDefs = _lib.DrawPopDefs
DrawPopDefs.restype = None
DrawPopDefs.argtypes = [POINTER(DrawingWand)]
DrawPushClipPath = _lib.DrawPushClipPath
DrawPushClipPath.restype = None
DrawPushClipPath.argtypes = [POINTER(DrawingWand), STRING]
DrawPushDefs = _lib.DrawPushDefs
DrawPushDefs.restype = None
DrawPushDefs.argtypes = [POINTER(DrawingWand)]
DrawRectangle = _lib.DrawRectangle
DrawRectangle.restype = None
DrawRectangle.argtypes = [POINTER(DrawingWand), c_double, c_double, c_double, c_double]
DrawResetVectorGraphics = _lib.DrawResetVectorGraphics
DrawResetVectorGraphics.restype = None
DrawResetVectorGraphics.argtypes = [POINTER(DrawingWand)]
DrawRotate = _lib.DrawRotate
DrawRotate.restype = None
DrawRotate.argtypes = [POINTER(DrawingWand), c_double]
DrawRoundRectangle = _lib.DrawRoundRectangle
DrawRoundRectangle.restype = None
DrawRoundRectangle.argtypes = [POINTER(DrawingWand), c_double, c_double, c_double, c_double, c_double, c_double]
DrawScale = _lib.DrawScale
DrawScale.restype = None
DrawScale.argtypes = [POINTER(DrawingWand), c_double, c_double]
DrawSetBorderColor = _lib.DrawSetBorderColor
DrawSetBorderColor.restype = None
DrawSetBorderColor.argtypes = [POINTER(DrawingWand), POINTER(PixelWand)]
DrawSetClipRule = _lib.DrawSetClipRule
DrawSetClipRule.restype = None
DrawSetClipRule.argtypes = [POINTER(DrawingWand), FillRule]
DrawSetClipUnits = _lib.DrawSetClipUnits
DrawSetClipUnits.restype = None
DrawSetClipUnits.argtypes = [POINTER(DrawingWand), ClipPathUnits]
DrawSetFillColor = _lib.DrawSetFillColor
DrawSetFillColor.restype = None
DrawSetFillColor.argtypes = [POINTER(DrawingWand), POINTER(PixelWand)]
DrawSetFillOpacity = _lib.DrawSetFillOpacity
DrawSetFillOpacity.restype = None
DrawSetFillOpacity.argtypes = [POINTER(DrawingWand), c_double]
DrawSetFillRule = _lib.DrawSetFillRule
DrawSetFillRule.restype = None
DrawSetFillRule.argtypes = [POINTER(DrawingWand), FillRule]
DrawSetFontSize = _lib.DrawSetFontSize
DrawSetFontSize.restype = None
DrawSetFontSize.argtypes = [POINTER(DrawingWand), c_double]
DrawSetFontStretch = _lib.DrawSetFontStretch
DrawSetFontStretch.restype = None
DrawSetFontStretch.argtypes = [POINTER(DrawingWand), StretchType]
DrawSetFontStyle = _lib.DrawSetFontStyle
DrawSetFontStyle.restype = None
DrawSetFontStyle.argtypes = [POINTER(DrawingWand), StyleType]
DrawSetFontWeight = _lib.DrawSetFontWeight
DrawSetFontWeight.restype = None
DrawSetFontWeight.argtypes = [POINTER(DrawingWand), size_t]
DrawSetGravity = _lib.DrawSetGravity
DrawSetGravity.restype = None
DrawSetGravity.argtypes = [POINTER(DrawingWand), GravityType]
DrawSetOpacity = _lib.DrawSetOpacity
DrawSetOpacity.restype = None
DrawSetOpacity.argtypes = [POINTER(DrawingWand), c_double]
DrawSetStrokeAntialias = _lib.DrawSetStrokeAntialias
DrawSetStrokeAntialias.restype = None
DrawSetStrokeAntialias.argtypes = [POINTER(DrawingWand), MagickBooleanType]
DrawSetStrokeColor = _lib.DrawSetStrokeColor
DrawSetStrokeColor.restype = None
DrawSetStrokeColor.argtypes = [POINTER(DrawingWand), POINTER(PixelWand)]
DrawSetStrokeDashOffset = _lib.DrawSetStrokeDashOffset
DrawSetStrokeDashOffset.restype = None
DrawSetStrokeDashOffset.argtypes = [POINTER(DrawingWand), c_double]
DrawSetStrokeLineCap = _lib.DrawSetStrokeLineCap
DrawSetStrokeLineCap.restype = None
DrawSetStrokeLineCap.argtypes = [POINTER(DrawingWand), LineCap]
DrawSetStrokeLineJoin = _lib.DrawSetStrokeLineJoin
DrawSetStrokeLineJoin.restype = None
DrawSetStrokeLineJoin.argtypes = [POINTER(DrawingWand), LineJoin]
DrawSetStrokeMiterLimit = _lib.DrawSetStrokeMiterLimit
DrawSetStrokeMiterLimit.restype = None
DrawSetStrokeMiterLimit.argtypes = [POINTER(DrawingWand), size_t]
DrawSetStrokeOpacity = _lib.DrawSetStrokeOpacity
DrawSetStrokeOpacity.restype = None
DrawSetStrokeOpacity.argtypes = [POINTER(DrawingWand), c_double]
DrawSetStrokeWidth = _lib.DrawSetStrokeWidth
DrawSetStrokeWidth.restype = None
DrawSetStrokeWidth.argtypes = [POINTER(DrawingWand), c_double]
DrawSetTextAlignment = _lib.DrawSetTextAlignment
DrawSetTextAlignment.restype = None
DrawSetTextAlignment.argtypes = [POINTER(DrawingWand), AlignType]
DrawSetTextAntialias = _lib.DrawSetTextAntialias
DrawSetTextAntialias.restype = None
DrawSetTextAntialias.argtypes = [POINTER(DrawingWand), MagickBooleanType]
DrawSetTextDecoration = _lib.DrawSetTextDecoration
DrawSetTextDecoration.restype = None
DrawSetTextDecoration.argtypes = [POINTER(DrawingWand), DecorationType]
DrawSetTextEncoding = _lib.DrawSetTextEncoding
DrawSetTextEncoding.restype = None
DrawSetTextEncoding.argtypes = [POINTER(DrawingWand), STRING]
DrawSetTextUnderColor = _lib.DrawSetTextUnderColor
DrawSetTextUnderColor.restype = None
DrawSetTextUnderColor.argtypes = [POINTER(DrawingWand), POINTER(PixelWand)]
DrawSetViewbox = _lib.DrawSetViewbox
DrawSetViewbox.restype = None
DrawSetViewbox.argtypes = [POINTER(DrawingWand), ssize_t, ssize_t, ssize_t, ssize_t]
DrawSkewX = _lib.DrawSkewX
DrawSkewX.restype = None
DrawSkewX.argtypes = [POINTER(DrawingWand), c_double]
DrawSkewY = _lib.DrawSkewY
DrawSkewY.restype = None
DrawSkewY.argtypes = [POINTER(DrawingWand), c_double]
DrawTranslate = _lib.DrawTranslate
DrawTranslate.restype = None
DrawTranslate.argtypes = [POINTER(DrawingWand), c_double, c_double]
IdentifyImageCommand = _lib.IdentifyImageCommand
IdentifyImageCommand.restype = MagickBooleanType
IdentifyImageCommand.argtypes = [POINTER(ImageInfo), c_int, POINTER(STRING), POINTER(STRING), POINTER(ExceptionInfo)]
ImportImageCommand = _lib.ImportImageCommand
ImportImageCommand.restype = MagickBooleanType
ImportImageCommand.argtypes = [POINTER(ImageInfo), c_int, POINTER(STRING), POINTER(STRING), POINTER(ExceptionInfo)]
MagickGetImageChannelFeatures = _lib.MagickGetImageChannelFeatures
MagickGetImageChannelFeatures.restype = POINTER(ChannelFeatures)
MagickGetImageChannelFeatures.argtypes = [POINTER(MagickWand), size_t]
MagickGetImageChannelStatistics = _lib.MagickGetImageChannelStatistics
MagickGetImageChannelStatistics.restype = POINTER(ChannelStatistics)
MagickGetImageChannelStatistics.argtypes = [POINTER(MagickWand)]
MagickGetImageFilename = _lib.MagickGetImageFilename
MagickGetImageFilename.restype = STRING
MagickGetImageFilename.argtypes = [POINTER(MagickWand)]
MagickGetImageFormat = _lib.MagickGetImageFormat
MagickGetImageFormat.restype = STRING
MagickGetImageFormat.argtypes = [POINTER(MagickWand)]
MagickGetImageSignature = _lib.MagickGetImageSignature
MagickGetImageSignature.restype = STRING
MagickGetImageSignature.argtypes = [POINTER(MagickWand)]
MagickIdentifyImage = _lib.MagickIdentifyImage
MagickIdentifyImage.restype = STRING
MagickIdentifyImage.argtypes = [POINTER(MagickWand)]
MagickGetImageColorspace = _lib.MagickGetImageColorspace
MagickGetImageColorspace.restype = ColorspaceType
MagickGetImageColorspace.argtypes = [POINTER(MagickWand)]
MagickGetImageCompose = _lib.MagickGetImageCompose
MagickGetImageCompose.restype = CompositeOperator
MagickGetImageCompose.argtypes = [POINTER(MagickWand)]
MagickGetImageCompression = _lib.MagickGetImageCompression
MagickGetImageCompression.restype = CompressionType
MagickGetImageCompression.argtypes = [POINTER(MagickWand)]
MagickGetImageDispose = _lib.MagickGetImageDispose
MagickGetImageDispose.restype = DisposeType
MagickGetImageDispose.argtypes = [POINTER(MagickWand)]
MagickGetImageChannelDistortions = _lib.MagickGetImageChannelDistortions
MagickGetImageChannelDistortions.restype = POINTER(c_double)
MagickGetImageChannelDistortions.argtypes = [POINTER(MagickWand), POINTER(MagickWand), MetricType]
MagickGetImageFuzz = _lib.MagickGetImageFuzz
MagickGetImageFuzz.restype = c_double
MagickGetImageFuzz.argtypes = [POINTER(MagickWand)]
MagickGetImageGamma = _lib.MagickGetImageGamma
MagickGetImageGamma.restype = c_double
MagickGetImageGamma.argtypes = [POINTER(MagickWand)]
MagickGetImageTotalInkDensity = _lib.MagickGetImageTotalInkDensity
MagickGetImageTotalInkDensity.restype = c_double
MagickGetImageTotalInkDensity.argtypes = [POINTER(MagickWand)]
MagickGetImageGravity = _lib.MagickGetImageGravity
MagickGetImageGravity.restype = GravityType
MagickGetImageGravity.argtypes = [POINTER(MagickWand)]
MagickDestroyImage = _lib.MagickDestroyImage
MagickDestroyImage.restype = POINTER(Image)
MagickDestroyImage.argtypes = [POINTER(Image)]
GetImageFromMagickWand = _lib.GetImageFromMagickWand
GetImageFromMagickWand.restype = POINTER(Image)
GetImageFromMagickWand.argtypes = [POINTER(MagickWand)]
MagickGetImageType = _lib.MagickGetImageType
MagickGetImageType.restype = ImageType
MagickGetImageType.argtypes = [POINTER(MagickWand)]
MagickGetImageInterlaceScheme = _lib.MagickGetImageInterlaceScheme
MagickGetImageInterlaceScheme.restype = InterlaceType
MagickGetImageInterlaceScheme.argtypes = [POINTER(MagickWand)]
MagickGetImageInterpolateMethod = _lib.MagickGetImageInterpolateMethod
MagickGetImageInterpolateMethod.restype = InterpolatePixelMethod
MagickGetImageInterpolateMethod.argtypes = [POINTER(MagickWand)]
MagickAdaptiveBlurImage = _lib.MagickAdaptiveBlurImage
MagickAdaptiveBlurImage.restype = MagickBooleanType
MagickAdaptiveBlurImage.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickAdaptiveBlurImageChannel = _lib.MagickAdaptiveBlurImageChannel
MagickAdaptiveBlurImageChannel.restype = MagickBooleanType
MagickAdaptiveBlurImageChannel.argtypes = [POINTER(MagickWand), ChannelType, c_double, c_double]
MagickAdaptiveResizeImage = _lib.MagickAdaptiveResizeImage
MagickAdaptiveResizeImage.restype = MagickBooleanType
MagickAdaptiveResizeImage.argtypes = [POINTER(MagickWand), size_t, size_t]
MagickAdaptiveSharpenImage = _lib.MagickAdaptiveSharpenImage
MagickAdaptiveSharpenImage.restype = MagickBooleanType
MagickAdaptiveSharpenImage.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickAdaptiveSharpenImageChannel = _lib.MagickAdaptiveSharpenImageChannel
MagickAdaptiveSharpenImageChannel.restype = MagickBooleanType
MagickAdaptiveSharpenImageChannel.argtypes = [POINTER(MagickWand), ChannelType, c_double, c_double]
MagickAdaptiveThresholdImage = _lib.MagickAdaptiveThresholdImage
MagickAdaptiveThresholdImage.restype = MagickBooleanType
MagickAdaptiveThresholdImage.argtypes = [POINTER(MagickWand), size_t, size_t, ssize_t]
MagickAddImage = _lib.MagickAddImage
MagickAddImage.restype = MagickBooleanType
MagickAddImage.argtypes = [POINTER(MagickWand), POINTER(MagickWand)]
MagickAddNoiseImage = _lib.MagickAddNoiseImage
MagickAddNoiseImage.restype = MagickBooleanType
MagickAddNoiseImage.argtypes = [POINTER(MagickWand), NoiseType]
MagickAddNoiseImageChannel = _lib.MagickAddNoiseImageChannel
MagickAddNoiseImageChannel.restype = MagickBooleanType
MagickAddNoiseImageChannel.argtypes = [POINTER(MagickWand), ChannelType, NoiseType]
MagickAffineTransformImage = _lib.MagickAffineTransformImage
MagickAffineTransformImage.restype = MagickBooleanType
MagickAffineTransformImage.argtypes = [POINTER(MagickWand), POINTER(DrawingWand)]
MagickAnnotateImage = _lib.MagickAnnotateImage
MagickAnnotateImage.restype = MagickBooleanType
MagickAnnotateImage.argtypes = [POINTER(MagickWand), POINTER(DrawingWand), c_double, c_double, c_double, STRING]
MagickAnimateImages = _lib.MagickAnimateImages
MagickAnimateImages.restype = MagickBooleanType
MagickAnimateImages.argtypes = [POINTER(MagickWand), STRING]
MagickAutoGammaImage = _lib.MagickAutoGammaImage
MagickAutoGammaImage.restype = MagickBooleanType
MagickAutoGammaImage.argtypes = [POINTER(MagickWand)]
MagickAutoGammaImageChannel = _lib.MagickAutoGammaImageChannel
MagickAutoGammaImageChannel.restype = MagickBooleanType
MagickAutoGammaImageChannel.argtypes = [POINTER(MagickWand), ChannelType]
MagickAutoLevelImage = _lib.MagickAutoLevelImage
MagickAutoLevelImage.restype = MagickBooleanType
MagickAutoLevelImage.argtypes = [POINTER(MagickWand)]
MagickAutoLevelImageChannel = _lib.MagickAutoLevelImageChannel
MagickAutoLevelImageChannel.restype = MagickBooleanType
MagickAutoLevelImageChannel.argtypes = [POINTER(MagickWand), ChannelType]
MagickBlackThresholdImage = _lib.MagickBlackThresholdImage
MagickBlackThresholdImage.restype = MagickBooleanType
MagickBlackThresholdImage.argtypes = [POINTER(MagickWand), POINTER(PixelWand)]
MagickBlueShiftImage = _lib.MagickBlueShiftImage
MagickBlueShiftImage.restype = MagickBooleanType
MagickBlueShiftImage.argtypes = [POINTER(MagickWand), c_double]
MagickBlurImage = _lib.MagickBlurImage
MagickBlurImage.restype = MagickBooleanType
MagickBlurImage.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickBlurImageChannel = _lib.MagickBlurImageChannel
MagickBlurImageChannel.restype = MagickBooleanType
MagickBlurImageChannel.argtypes = [POINTER(MagickWand), ChannelType, c_double, c_double]
MagickBorderImage = _lib.MagickBorderImage
MagickBorderImage.restype = MagickBooleanType
MagickBorderImage.argtypes = [POINTER(MagickWand), POINTER(PixelWand), size_t, size_t]
MagickBrightnessContrastImage = _lib.MagickBrightnessContrastImage
MagickBrightnessContrastImage.restype = MagickBooleanType
MagickBrightnessContrastImage.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickBrightnessContrastImageChannel = _lib.MagickBrightnessContrastImageChannel
MagickBrightnessContrastImageChannel.restype = MagickBooleanType
MagickBrightnessContrastImageChannel.argtypes = [POINTER(MagickWand), ChannelType, c_double, c_double]
MagickCharcoalImage = _lib.MagickCharcoalImage
MagickCharcoalImage.restype = MagickBooleanType
MagickCharcoalImage.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickChopImage = _lib.MagickChopImage
MagickChopImage.restype = MagickBooleanType
MagickChopImage.argtypes = [POINTER(MagickWand), size_t, size_t, ssize_t, ssize_t]
MagickClampImage = _lib.MagickClampImage
MagickClampImage.restype = MagickBooleanType
MagickClampImage.argtypes = [POINTER(MagickWand)]
MagickClampImageChannel = _lib.MagickClampImageChannel
MagickClampImageChannel.restype = MagickBooleanType
MagickClampImageChannel.argtypes = [POINTER(MagickWand), ChannelType]
MagickClipImage = _lib.MagickClipImage
MagickClipImage.restype = MagickBooleanType
MagickClipImage.argtypes = [POINTER(MagickWand)]
MagickClipImagePath = _lib.MagickClipImagePath
MagickClipImagePath.restype = MagickBooleanType
MagickClipImagePath.argtypes = [POINTER(MagickWand), STRING, MagickBooleanType]
MagickClutImage = _lib.MagickClutImage
MagickClutImage.restype = MagickBooleanType
MagickClutImage.argtypes = [POINTER(MagickWand), POINTER(MagickWand)]
MagickClutImageChannel = _lib.MagickClutImageChannel
MagickClutImageChannel.restype = MagickBooleanType
MagickClutImageChannel.argtypes = [POINTER(MagickWand), ChannelType, POINTER(MagickWand)]
MagickColorDecisionListImage = _lib.MagickColorDecisionListImage
MagickColorDecisionListImage.restype = MagickBooleanType
MagickColorDecisionListImage.argtypes = [POINTER(MagickWand), STRING]
MagickColorizeImage = _lib.MagickColorizeImage
MagickColorizeImage.restype = MagickBooleanType
MagickColorizeImage.argtypes = [POINTER(MagickWand), POINTER(PixelWand), POINTER(PixelWand)]
MagickColorMatrixImage = _lib.MagickColorMatrixImage
MagickColorMatrixImage.restype = MagickBooleanType
MagickColorMatrixImage.argtypes = [POINTER(MagickWand), POINTER(KernelInfo)]
MagickCommentImage = _lib.MagickCommentImage
MagickCommentImage.restype = MagickBooleanType
MagickCommentImage.argtypes = [POINTER(MagickWand), STRING]
MagickCompositeImage = _lib.MagickCompositeImage
MagickCompositeImage.restype = MagickBooleanType
MagickCompositeImage.argtypes = [POINTER(MagickWand), POINTER(MagickWand), CompositeOperator, ssize_t, ssize_t]
MagickCompositeImageChannel = _lib.MagickCompositeImageChannel
MagickCompositeImageChannel.restype = MagickBooleanType
MagickCompositeImageChannel.argtypes = [POINTER(MagickWand), ChannelType, POINTER(MagickWand), CompositeOperator, ssize_t, ssize_t]
MagickConstituteImage = _lib.MagickConstituteImage
MagickConstituteImage.restype = MagickBooleanType
MagickConstituteImage.argtypes = [POINTER(MagickWand), size_t, size_t, STRING, StorageType, c_void_p]
MagickContrastImage = _lib.MagickContrastImage
MagickContrastImage.restype = MagickBooleanType
MagickContrastImage.argtypes = [POINTER(MagickWand), MagickBooleanType]
MagickContrastStretchImage = _lib.MagickContrastStretchImage
MagickContrastStretchImage.restype = MagickBooleanType
MagickContrastStretchImage.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickContrastStretchImageChannel = _lib.MagickContrastStretchImageChannel
MagickContrastStretchImageChannel.restype = MagickBooleanType
MagickContrastStretchImageChannel.argtypes = [POINTER(MagickWand), ChannelType, c_double, c_double]
MagickConvolveImage = _lib.MagickConvolveImage
MagickConvolveImage.restype = MagickBooleanType
MagickConvolveImage.argtypes = [POINTER(MagickWand), size_t, POINTER(c_double)]
MagickConvolveImageChannel = _lib.MagickConvolveImageChannel
MagickConvolveImageChannel.restype = MagickBooleanType
MagickConvolveImageChannel.argtypes = [POINTER(MagickWand), ChannelType, size_t, POINTER(c_double)]
MagickCropImage = _lib.MagickCropImage
MagickCropImage.restype = MagickBooleanType
MagickCropImage.argtypes = [POINTER(MagickWand), size_t, size_t, ssize_t, ssize_t]
MagickCycleColormapImage = _lib.MagickCycleColormapImage
MagickCycleColormapImage.restype = MagickBooleanType
MagickCycleColormapImage.argtypes = [POINTER(MagickWand), ssize_t]
MagickDecipherImage = _lib.MagickDecipherImage
MagickDecipherImage.restype = MagickBooleanType
MagickDecipherImage.argtypes = [POINTER(MagickWand), STRING]
MagickDeskewImage = _lib.MagickDeskewImage
MagickDeskewImage.restype = MagickBooleanType
MagickDeskewImage.argtypes = [POINTER(MagickWand), c_double]
MagickDespeckleImage = _lib.MagickDespeckleImage
MagickDespeckleImage.restype = MagickBooleanType
MagickDespeckleImage.argtypes = [POINTER(MagickWand)]
MagickDisplayImage = _lib.MagickDisplayImage
MagickDisplayImage.restype = MagickBooleanType
MagickDisplayImage.argtypes = [POINTER(MagickWand), STRING]
MagickDisplayImages = _lib.MagickDisplayImages
MagickDisplayImages.restype = MagickBooleanType
MagickDisplayImages.argtypes = [POINTER(MagickWand), STRING]
MagickDistortImage = _lib.MagickDistortImage
MagickDistortImage.restype = MagickBooleanType
MagickDistortImage.argtypes = [POINTER(MagickWand), DistortImageMethod, size_t, POINTER(c_double), MagickBooleanType]
MagickDrawImage = _lib.MagickDrawImage
MagickDrawImage.restype = MagickBooleanType
MagickDrawImage.argtypes = [POINTER(MagickWand), POINTER(DrawingWand)]
MagickEdgeImage = _lib.MagickEdgeImage
MagickEdgeImage.restype = MagickBooleanType
MagickEdgeImage.argtypes = [POINTER(MagickWand), c_double]
MagickEmbossImage = _lib.MagickEmbossImage
MagickEmbossImage.restype = MagickBooleanType
MagickEmbossImage.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickEncipherImage = _lib.MagickEncipherImage
MagickEncipherImage.restype = MagickBooleanType
MagickEncipherImage.argtypes = [POINTER(MagickWand), STRING]
MagickEnhanceImage = _lib.MagickEnhanceImage
MagickEnhanceImage.restype = MagickBooleanType
MagickEnhanceImage.argtypes = [POINTER(MagickWand)]
MagickEqualizeImage = _lib.MagickEqualizeImage
MagickEqualizeImage.restype = MagickBooleanType
MagickEqualizeImage.argtypes = [POINTER(MagickWand)]
MagickEqualizeImageChannel = _lib.MagickEqualizeImageChannel
MagickEqualizeImageChannel.restype = MagickBooleanType
MagickEqualizeImageChannel.argtypes = [POINTER(MagickWand), ChannelType]
MagickEvaluateImage = _lib.MagickEvaluateImage
MagickEvaluateImage.restype = MagickBooleanType
MagickEvaluateImage.argtypes = [POINTER(MagickWand), MagickEvaluateOperator, c_double]
MagickEvaluateImageChannel = _lib.MagickEvaluateImageChannel
MagickEvaluateImageChannel.restype = MagickBooleanType
MagickEvaluateImageChannel.argtypes = [POINTER(MagickWand), ChannelType, MagickEvaluateOperator, c_double]
MagickExportImagePixels = _lib.MagickExportImagePixels
MagickExportImagePixels.restype = MagickBooleanType
MagickExportImagePixels.argtypes = [POINTER(MagickWand), ssize_t, ssize_t, size_t, size_t, STRING, StorageType, c_void_p]
MagickExtentImage = _lib.MagickExtentImage
MagickExtentImage.restype = MagickBooleanType
MagickExtentImage.argtypes = [POINTER(MagickWand), size_t, size_t, ssize_t, ssize_t]
MagickFilterImage = _lib.MagickFilterImage
MagickFilterImage.restype = MagickBooleanType
MagickFilterImage.argtypes = [POINTER(MagickWand), POINTER(KernelInfo)]
MagickFilterImageChannel = _lib.MagickFilterImageChannel
MagickFilterImageChannel.restype = MagickBooleanType
MagickFilterImageChannel.argtypes = [POINTER(MagickWand), ChannelType, POINTER(KernelInfo)]
MagickFlipImage = _lib.MagickFlipImage
MagickFlipImage.restype = MagickBooleanType
MagickFlipImage.argtypes = [POINTER(MagickWand)]
MagickFloodfillPaintImage = _lib.MagickFloodfillPaintImage
MagickFloodfillPaintImage.restype = MagickBooleanType
MagickFloodfillPaintImage.argtypes = [POINTER(MagickWand), ChannelType, POINTER(PixelWand), c_double, POINTER(PixelWand), ssize_t, ssize_t, MagickBooleanType]
MagickFlopImage = _lib.MagickFlopImage
MagickFlopImage.restype = MagickBooleanType
MagickFlopImage.argtypes = [POINTER(MagickWand)]
MagickForwardFourierTransformImage = _lib.MagickForwardFourierTransformImage
MagickForwardFourierTransformImage.restype = MagickBooleanType
MagickForwardFourierTransformImage.argtypes = [POINTER(MagickWand), MagickBooleanType]
MagickFrameImage = _lib.MagickFrameImage
MagickFrameImage.restype = MagickBooleanType
MagickFrameImage.argtypes = [POINTER(MagickWand), POINTER(PixelWand), size_t, size_t, ssize_t, ssize_t]
MagickFunctionImage = _lib.MagickFunctionImage
MagickFunctionImage.restype = MagickBooleanType
MagickFunctionImage.argtypes = [POINTER(MagickWand), MagickFunction, size_t, POINTER(c_double)]
MagickFunctionImageChannel = _lib.MagickFunctionImageChannel
MagickFunctionImageChannel.restype = MagickBooleanType
MagickFunctionImageChannel.argtypes = [POINTER(MagickWand), ChannelType, MagickFunction, size_t, POINTER(c_double)]
MagickGammaImage = _lib.MagickGammaImage
MagickGammaImage.restype = MagickBooleanType
MagickGammaImage.argtypes = [POINTER(MagickWand), c_double]
MagickGammaImageChannel = _lib.MagickGammaImageChannel
MagickGammaImageChannel.restype = MagickBooleanType
MagickGammaImageChannel.argtypes = [POINTER(MagickWand), ChannelType, c_double]
MagickGaussianBlurImage = _lib.MagickGaussianBlurImage
MagickGaussianBlurImage.restype = MagickBooleanType
MagickGaussianBlurImage.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickGaussianBlurImageChannel = _lib.MagickGaussianBlurImageChannel
MagickGaussianBlurImageChannel.restype = MagickBooleanType
MagickGaussianBlurImageChannel.argtypes = [POINTER(MagickWand), ChannelType, c_double, c_double]
MagickGetImageAlphaChannel = _lib.MagickGetImageAlphaChannel
MagickGetImageAlphaChannel.restype = MagickBooleanType
MagickGetImageAlphaChannel.argtypes = [POINTER(MagickWand)]
MagickGetImageBackgroundColor = _lib.MagickGetImageBackgroundColor
MagickGetImageBackgroundColor.restype = MagickBooleanType
MagickGetImageBackgroundColor.argtypes = [POINTER(MagickWand), POINTER(PixelWand)]
MagickGetImageBluePrimary = _lib.MagickGetImageBluePrimary
MagickGetImageBluePrimary.restype = MagickBooleanType
MagickGetImageBluePrimary.argtypes = [POINTER(MagickWand), POINTER(c_double), POINTER(c_double)]
MagickGetImageBorderColor = _lib.MagickGetImageBorderColor
MagickGetImageBorderColor.restype = MagickBooleanType
MagickGetImageBorderColor.argtypes = [POINTER(MagickWand), POINTER(PixelWand)]
MagickGetImageChannelDistortion = _lib.MagickGetImageChannelDistortion
MagickGetImageChannelDistortion.restype = MagickBooleanType
MagickGetImageChannelDistortion.argtypes = [POINTER(MagickWand), POINTER(MagickWand), ChannelType, MetricType, POINTER(c_double)]
MagickGetImageChannelKurtosis = _lib.MagickGetImageChannelKurtosis
MagickGetImageChannelKurtosis.restype = MagickBooleanType
MagickGetImageChannelKurtosis.argtypes = [POINTER(MagickWand), ChannelType, POINTER(c_double), POINTER(c_double)]
MagickGetImageChannelMean = _lib.MagickGetImageChannelMean
MagickGetImageChannelMean.restype = MagickBooleanType
MagickGetImageChannelMean.argtypes = [POINTER(MagickWand), ChannelType, POINTER(c_double), POINTER(c_double)]
MagickGetImageChannelRange = _lib.MagickGetImageChannelRange
MagickGetImageChannelRange.restype = MagickBooleanType
MagickGetImageChannelRange.argtypes = [POINTER(MagickWand), ChannelType, POINTER(c_double), POINTER(c_double)]
MagickGetImageColormapColor = _lib.MagickGetImageColormapColor
MagickGetImageColormapColor.restype = MagickBooleanType
MagickGetImageColormapColor.argtypes = [POINTER(MagickWand), size_t, POINTER(PixelWand)]
MagickGetImageDistortion = _lib.MagickGetImageDistortion
MagickGetImageDistortion.restype = MagickBooleanType
MagickGetImageDistortion.argtypes = [POINTER(MagickWand), POINTER(MagickWand), MetricType, POINTER(c_double)]
MagickGetImageGreenPrimary = _lib.MagickGetImageGreenPrimary
MagickGetImageGreenPrimary.restype = MagickBooleanType
MagickGetImageGreenPrimary.argtypes = [POINTER(MagickWand), POINTER(c_double), POINTER(c_double)]
MagickGetImageMatteColor = _lib.MagickGetImageMatteColor
MagickGetImageMatteColor.restype = MagickBooleanType
MagickGetImageMatteColor.argtypes = [POINTER(MagickWand), POINTER(PixelWand)]
MagickGetImageLength = _lib.MagickGetImageLength
MagickGetImageLength.restype = MagickBooleanType
MagickGetImageLength.argtypes = [POINTER(MagickWand), POINTER(MagickSizeType)]
MagickGetImagePage = _lib.MagickGetImagePage
MagickGetImagePage.restype = MagickBooleanType
MagickGetImagePage.argtypes = [POINTER(MagickWand), POINTER(size_t), POINTER(size_t), POINTER(ssize_t), POINTER(ssize_t)]
MagickGetImagePixelColor = _lib.MagickGetImagePixelColor
MagickGetImagePixelColor.restype = MagickBooleanType
MagickGetImagePixelColor.argtypes = [POINTER(MagickWand), ssize_t, ssize_t, POINTER(PixelWand)]
MagickGetImageRange = _lib.MagickGetImageRange
MagickGetImageRange.restype = MagickBooleanType
MagickGetImageRange.argtypes = [POINTER(MagickWand), POINTER(c_double), POINTER(c_double)]
MagickGetImageRedPrimary = _lib.MagickGetImageRedPrimary
MagickGetImageRedPrimary.restype = MagickBooleanType
MagickGetImageRedPrimary.argtypes = [POINTER(MagickWand), POINTER(c_double), POINTER(c_double)]
MagickGetImageResolution = _lib.MagickGetImageResolution
MagickGetImageResolution.restype = MagickBooleanType
MagickGetImageResolution.argtypes = [POINTER(MagickWand), POINTER(c_double), POINTER(c_double)]
MagickGetImageWhitePoint = _lib.MagickGetImageWhitePoint
MagickGetImageWhitePoint.restype = MagickBooleanType
MagickGetImageWhitePoint.argtypes = [POINTER(MagickWand), POINTER(c_double), POINTER(c_double)]
MagickHaldClutImage = _lib.MagickHaldClutImage
MagickHaldClutImage.restype = MagickBooleanType
MagickHaldClutImage.argtypes = [POINTER(MagickWand), POINTER(MagickWand)]
MagickHaldClutImageChannel = _lib.MagickHaldClutImageChannel
MagickHaldClutImageChannel.restype = MagickBooleanType
MagickHaldClutImageChannel.argtypes = [POINTER(MagickWand), ChannelType, POINTER(MagickWand)]
MagickHasNextImage = _lib.MagickHasNextImage
MagickHasNextImage.restype = MagickBooleanType
MagickHasNextImage.argtypes = [POINTER(MagickWand)]
MagickHasPreviousImage = _lib.MagickHasPreviousImage
MagickHasPreviousImage.restype = MagickBooleanType
MagickHasPreviousImage.argtypes = [POINTER(MagickWand)]
MagickImplodeImage = _lib.MagickImplodeImage
MagickImplodeImage.restype = MagickBooleanType
MagickImplodeImage.argtypes = [POINTER(MagickWand), c_double]
MagickImportImagePixels = _lib.MagickImportImagePixels
MagickImportImagePixels.restype = MagickBooleanType
MagickImportImagePixels.argtypes = [POINTER(MagickWand), ssize_t, ssize_t, size_t, size_t, STRING, StorageType, c_void_p]
MagickInverseFourierTransformImage = _lib.MagickInverseFourierTransformImage
MagickInverseFourierTransformImage.restype = MagickBooleanType
MagickInverseFourierTransformImage.argtypes = [POINTER(MagickWand), POINTER(MagickWand), MagickBooleanType]
MagickLabelImage = _lib.MagickLabelImage
MagickLabelImage.restype = MagickBooleanType
MagickLabelImage.argtypes = [POINTER(MagickWand), STRING]
MagickLevelImage = _lib.MagickLevelImage
MagickLevelImage.restype = MagickBooleanType
MagickLevelImage.argtypes = [POINTER(MagickWand), c_double, c_double, c_double]
MagickLevelImageChannel = _lib.MagickLevelImageChannel
MagickLevelImageChannel.restype = MagickBooleanType
MagickLevelImageChannel.argtypes = [POINTER(MagickWand), ChannelType, c_double, c_double, c_double]
MagickLinearStretchImage = _lib.MagickLinearStretchImage
MagickLinearStretchImage.restype = MagickBooleanType
MagickLinearStretchImage.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickLiquidRescaleImage = _lib.MagickLiquidRescaleImage
MagickLiquidRescaleImage.restype = MagickBooleanType
MagickLiquidRescaleImage.argtypes = [POINTER(MagickWand), size_t, size_t, c_double, c_double]
MagickMagnifyImage = _lib.MagickMagnifyImage
MagickMagnifyImage.restype = MagickBooleanType
MagickMagnifyImage.argtypes = [POINTER(MagickWand)]
MagickMedianFilterImage = _lib.MagickMedianFilterImage
MagickMedianFilterImage.restype = MagickBooleanType
MagickMedianFilterImage.argtypes = [POINTER(MagickWand), c_double]
MagickMinifyImage = _lib.MagickMinifyImage
MagickMinifyImage.restype = MagickBooleanType
MagickMinifyImage.argtypes = [POINTER(MagickWand)]
MagickModulateImage = _lib.MagickModulateImage
MagickModulateImage.restype = MagickBooleanType
MagickModulateImage.argtypes = [POINTER(MagickWand), c_double, c_double, c_double]
MagickMorphologyImage = _lib.MagickMorphologyImage
MagickMorphologyImage.restype = MagickBooleanType
MagickMorphologyImage.argtypes = [POINTER(MagickWand), MorphologyMethod, ssize_t, POINTER(KernelInfo)]
MagickMorphologyImageChannel = _lib.MagickMorphologyImageChannel
MagickMorphologyImageChannel.restype = MagickBooleanType
MagickMorphologyImageChannel.argtypes = [POINTER(MagickWand), ChannelType, MorphologyMethod, ssize_t, POINTER(KernelInfo)]
MagickMotionBlurImage = _lib.MagickMotionBlurImage
MagickMotionBlurImage.restype = MagickBooleanType
MagickMotionBlurImage.argtypes = [POINTER(MagickWand), c_double, c_double, c_double]
MagickMotionBlurImageChannel = _lib.MagickMotionBlurImageChannel
MagickMotionBlurImageChannel.restype = MagickBooleanType
MagickMotionBlurImageChannel.argtypes = [POINTER(MagickWand), ChannelType, c_double, c_double, c_double]
MagickNegateImage = _lib.MagickNegateImage
MagickNegateImage.restype = MagickBooleanType
MagickNegateImage.argtypes = [POINTER(MagickWand), MagickBooleanType]
MagickNegateImageChannel = _lib.MagickNegateImageChannel
MagickNegateImageChannel.restype = MagickBooleanType
MagickNegateImageChannel.argtypes = [POINTER(MagickWand), ChannelType, MagickBooleanType]
MagickNewImage = _lib.MagickNewImage
MagickNewImage.restype = MagickBooleanType
MagickNewImage.argtypes = [POINTER(MagickWand), size_t, size_t, POINTER(PixelWand)]
MagickNextImage = _lib.MagickNextImage
MagickNextImage.restype = MagickBooleanType
MagickNextImage.argtypes = [POINTER(MagickWand)]
MagickNormalizeImage = _lib.MagickNormalizeImage
MagickNormalizeImage.restype = MagickBooleanType
MagickNormalizeImage.argtypes = [POINTER(MagickWand)]
MagickNormalizeImageChannel = _lib.MagickNormalizeImageChannel
MagickNormalizeImageChannel.restype = MagickBooleanType
MagickNormalizeImageChannel.argtypes = [POINTER(MagickWand), ChannelType]
MagickOilPaintImage = _lib.MagickOilPaintImage
MagickOilPaintImage.restype = MagickBooleanType
MagickOilPaintImage.argtypes = [POINTER(MagickWand), c_double]
MagickOpaquePaintImage = _lib.MagickOpaquePaintImage
MagickOpaquePaintImage.restype = MagickBooleanType
MagickOpaquePaintImage.argtypes = [POINTER(MagickWand), POINTER(PixelWand), POINTER(PixelWand), c_double, MagickBooleanType]
MagickOpaquePaintImageChannel = _lib.MagickOpaquePaintImageChannel
MagickOpaquePaintImageChannel.restype = MagickBooleanType
MagickOpaquePaintImageChannel.argtypes = [POINTER(MagickWand), ChannelType, POINTER(PixelWand), POINTER(PixelWand), c_double, MagickBooleanType]
MagickOrderedPosterizeImage = _lib.MagickOrderedPosterizeImage
MagickOrderedPosterizeImage.restype = MagickBooleanType
MagickOrderedPosterizeImage.argtypes = [POINTER(MagickWand), STRING]
MagickOrderedPosterizeImageChannel = _lib.MagickOrderedPosterizeImageChannel
MagickOrderedPosterizeImageChannel.restype = MagickBooleanType
MagickOrderedPosterizeImageChannel.argtypes = [POINTER(MagickWand), ChannelType, STRING]
MagickTransparentPaintImage = _lib.MagickTransparentPaintImage
MagickTransparentPaintImage.restype = MagickBooleanType
MagickTransparentPaintImage.argtypes = [POINTER(MagickWand), POINTER(PixelWand), c_double, c_double, MagickBooleanType]
MagickPingImage = _lib.MagickPingImage
MagickPingImage.restype = MagickBooleanType
MagickPingImage.argtypes = [POINTER(MagickWand), STRING]
MagickPingImageBlob = _lib.MagickPingImageBlob
MagickPingImageBlob.restype = MagickBooleanType
MagickPingImageBlob.argtypes = [POINTER(MagickWand), c_void_p, size_t]
MagickPingImageFile = _lib.MagickPingImageFile
MagickPingImageFile.restype = MagickBooleanType
MagickPingImageFile.argtypes = [POINTER(MagickWand), POINTER(FILE)]
MagickPolaroidImage = _lib.MagickPolaroidImage
MagickPolaroidImage.restype = MagickBooleanType
MagickPolaroidImage.argtypes = [POINTER(MagickWand), POINTER(DrawingWand), c_double]
MagickPosterizeImage = _lib.MagickPosterizeImage
MagickPosterizeImage.restype = MagickBooleanType
MagickPosterizeImage.argtypes = [POINTER(MagickWand), size_t, MagickBooleanType]
MagickPreviousImage = _lib.MagickPreviousImage
MagickPreviousImage.restype = MagickBooleanType
MagickPreviousImage.argtypes = [POINTER(MagickWand)]
MagickQuantizeImage = _lib.MagickQuantizeImage
MagickQuantizeImage.restype = MagickBooleanType
MagickQuantizeImage.argtypes = [POINTER(MagickWand), size_t, ColorspaceType, size_t, MagickBooleanType, MagickBooleanType]
MagickQuantizeImages = _lib.MagickQuantizeImages
MagickQuantizeImages.restype = MagickBooleanType
MagickQuantizeImages.argtypes = [POINTER(MagickWand), size_t, ColorspaceType, size_t, MagickBooleanType, MagickBooleanType]
MagickRadialBlurImage = _lib.MagickRadialBlurImage
MagickRadialBlurImage.restype = MagickBooleanType
MagickRadialBlurImage.argtypes = [POINTER(MagickWand), c_double]
MagickRadialBlurImageChannel = _lib.MagickRadialBlurImageChannel
MagickRadialBlurImageChannel.restype = MagickBooleanType
MagickRadialBlurImageChannel.argtypes = [POINTER(MagickWand), ChannelType, c_double]
MagickRaiseImage = _lib.MagickRaiseImage
MagickRaiseImage.restype = MagickBooleanType
MagickRaiseImage.argtypes = [POINTER(MagickWand), size_t, size_t, ssize_t, ssize_t, MagickBooleanType]
MagickRandomThresholdImage = _lib.MagickRandomThresholdImage
MagickRandomThresholdImage.restype = MagickBooleanType
MagickRandomThresholdImage.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickRandomThresholdImageChannel = _lib.MagickRandomThresholdImageChannel
MagickRandomThresholdImageChannel.restype = MagickBooleanType
MagickRandomThresholdImageChannel.argtypes = [POINTER(MagickWand), ChannelType, c_double, c_double]
MagickReadImage = _lib.MagickReadImage
MagickReadImage.restype = MagickBooleanType
MagickReadImage.argtypes = [POINTER(MagickWand), STRING]
MagickReadImageBlob = _lib.MagickReadImageBlob
MagickReadImageBlob.restype = MagickBooleanType
MagickReadImageBlob.argtypes = [POINTER(MagickWand), c_void_p, size_t]
MagickReadImageFile = _lib.MagickReadImageFile
MagickReadImageFile.restype = MagickBooleanType
MagickReadImageFile.argtypes = [POINTER(MagickWand), POINTER(FILE)]
MagickReduceNoiseImage = _lib.MagickReduceNoiseImage
MagickReduceNoiseImage.restype = MagickBooleanType
MagickReduceNoiseImage.argtypes = [POINTER(MagickWand), c_double]
MagickRemapImage = _lib.MagickRemapImage
MagickRemapImage.restype = MagickBooleanType
MagickRemapImage.argtypes = [POINTER(MagickWand), POINTER(MagickWand), DitherMethod]
MagickRemoveImage = _lib.MagickRemoveImage
MagickRemoveImage.restype = MagickBooleanType
MagickRemoveImage.argtypes = [POINTER(MagickWand)]
MagickResampleImage = _lib.MagickResampleImage
MagickResampleImage.restype = MagickBooleanType
MagickResampleImage.argtypes = [POINTER(MagickWand), c_double, c_double, FilterTypes, c_double]
MagickResetImagePage = _lib.MagickResetImagePage
MagickResetImagePage.restype = MagickBooleanType
MagickResetImagePage.argtypes = [POINTER(MagickWand), STRING]
MagickResizeImage = _lib.MagickResizeImage
MagickResizeImage.restype = MagickBooleanType
MagickResizeImage.argtypes = [POINTER(MagickWand), size_t, size_t, FilterTypes, c_double]
MagickRollImage = _lib.MagickRollImage
MagickRollImage.restype = MagickBooleanType
MagickRollImage.argtypes = [POINTER(MagickWand), ssize_t, ssize_t]
MagickRotateImage = _lib.MagickRotateImage
MagickRotateImage.restype = MagickBooleanType
MagickRotateImage.argtypes = [POINTER(MagickWand), POINTER(PixelWand), c_double]
MagickSampleImage = _lib.MagickSampleImage
MagickSampleImage.restype = MagickBooleanType
MagickSampleImage.argtypes = [POINTER(MagickWand), size_t, size_t]
MagickScaleImage = _lib.MagickScaleImage
MagickScaleImage.restype = MagickBooleanType
MagickScaleImage.argtypes = [POINTER(MagickWand), size_t, size_t]
MagickSegmentImage = _lib.MagickSegmentImage
MagickSegmentImage.restype = MagickBooleanType
MagickSegmentImage.argtypes = [POINTER(MagickWand), ColorspaceType, MagickBooleanType, c_double, c_double]
MagickSelectiveBlurImage = _lib.MagickSelectiveBlurImage
MagickSelectiveBlurImage.restype = MagickBooleanType
MagickSelectiveBlurImage.argtypes = [POINTER(MagickWand), c_double, c_double, c_double]
MagickSelectiveBlurImageChannel = _lib.MagickSelectiveBlurImageChannel
MagickSelectiveBlurImageChannel.restype = MagickBooleanType
MagickSelectiveBlurImageChannel.argtypes = [POINTER(MagickWand), ChannelType, c_double, c_double, c_double]
MagickSeparateImageChannel = _lib.MagickSeparateImageChannel
MagickSeparateImageChannel.restype = MagickBooleanType
MagickSeparateImageChannel.argtypes = [POINTER(MagickWand), ChannelType]
MagickSepiaToneImage = _lib.MagickSepiaToneImage
MagickSepiaToneImage.restype = MagickBooleanType
MagickSepiaToneImage.argtypes = [POINTER(MagickWand), c_double]
MagickSetImage = _lib.MagickSetImage
MagickSetImage.restype = MagickBooleanType
MagickSetImage.argtypes = [POINTER(MagickWand), POINTER(MagickWand)]
MagickSetImageAlphaChannel = _lib.MagickSetImageAlphaChannel
MagickSetImageAlphaChannel.restype = MagickBooleanType
MagickSetImageAlphaChannel.argtypes = [POINTER(MagickWand), AlphaChannelType]
MagickSetImageBackgroundColor = _lib.MagickSetImageBackgroundColor
MagickSetImageBackgroundColor.restype = MagickBooleanType
MagickSetImageBackgroundColor.argtypes = [POINTER(MagickWand), POINTER(PixelWand)]
MagickSetImageBias = _lib.MagickSetImageBias
MagickSetImageBias.restype = MagickBooleanType
MagickSetImageBias.argtypes = [POINTER(MagickWand), c_double]
MagickSetImageBluePrimary = _lib.MagickSetImageBluePrimary
MagickSetImageBluePrimary.restype = MagickBooleanType
MagickSetImageBluePrimary.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickSetImageBorderColor = _lib.MagickSetImageBorderColor
MagickSetImageBorderColor.restype = MagickBooleanType
MagickSetImageBorderColor.argtypes = [POINTER(MagickWand), POINTER(PixelWand)]
MagickSetImageChannelDepth = _lib.MagickSetImageChannelDepth
MagickSetImageChannelDepth.restype = MagickBooleanType
MagickSetImageChannelDepth.argtypes = [POINTER(MagickWand), ChannelType, size_t]
MagickSetImageClipMask = _lib.MagickSetImageClipMask
MagickSetImageClipMask.restype = MagickBooleanType
MagickSetImageClipMask.argtypes = [POINTER(MagickWand), POINTER(MagickWand)]
MagickSetImageColor = _lib.MagickSetImageColor
MagickSetImageColor.restype = MagickBooleanType
MagickSetImageColor.argtypes = [POINTER(MagickWand), POINTER(PixelWand)]
MagickSetImageColormapColor = _lib.MagickSetImageColormapColor
MagickSetImageColormapColor.restype = MagickBooleanType
MagickSetImageColormapColor.argtypes = [POINTER(MagickWand), size_t, POINTER(PixelWand)]
MagickSetImageColorspace = _lib.MagickSetImageColorspace
MagickSetImageColorspace.restype = MagickBooleanType
MagickSetImageColorspace.argtypes = [POINTER(MagickWand), ColorspaceType]
MagickSetImageCompose = _lib.MagickSetImageCompose
MagickSetImageCompose.restype = MagickBooleanType
MagickSetImageCompose.argtypes = [POINTER(MagickWand), CompositeOperator]
MagickSetImageCompression = _lib.MagickSetImageCompression
MagickSetImageCompression.restype = MagickBooleanType
MagickSetImageCompression.argtypes = [POINTER(MagickWand), CompressionType]
MagickSetImageDelay = _lib.MagickSetImageDelay
MagickSetImageDelay.restype = MagickBooleanType
MagickSetImageDelay.argtypes = [POINTER(MagickWand), size_t]
MagickSetImageDepth = _lib.MagickSetImageDepth
MagickSetImageDepth.restype = MagickBooleanType
MagickSetImageDepth.argtypes = [POINTER(MagickWand), size_t]
MagickSetImageDispose = _lib.MagickSetImageDispose
MagickSetImageDispose.restype = MagickBooleanType
MagickSetImageDispose.argtypes = [POINTER(MagickWand), DisposeType]
MagickSetImageCompressionQuality = _lib.MagickSetImageCompressionQuality
MagickSetImageCompressionQuality.restype = MagickBooleanType
MagickSetImageCompressionQuality.argtypes = [POINTER(MagickWand), size_t]
MagickSetImageExtent = _lib.MagickSetImageExtent
MagickSetImageExtent.restype = MagickBooleanType
MagickSetImageExtent.argtypes = [POINTER(MagickWand), size_t, size_t]
MagickSetImageFilename = _lib.MagickSetImageFilename
MagickSetImageFilename.restype = MagickBooleanType
MagickSetImageFilename.argtypes = [POINTER(MagickWand), STRING]
MagickSetImageFormat = _lib.MagickSetImageFormat
MagickSetImageFormat.restype = MagickBooleanType
MagickSetImageFormat.argtypes = [POINTER(MagickWand), STRING]
MagickSetImageFuzz = _lib.MagickSetImageFuzz
MagickSetImageFuzz.restype = MagickBooleanType
MagickSetImageFuzz.argtypes = [POINTER(MagickWand), c_double]
MagickSetImageGamma = _lib.MagickSetImageGamma
MagickSetImageGamma.restype = MagickBooleanType
MagickSetImageGamma.argtypes = [POINTER(MagickWand), c_double]
MagickSetImageGravity = _lib.MagickSetImageGravity
MagickSetImageGravity.restype = MagickBooleanType
MagickSetImageGravity.argtypes = [POINTER(MagickWand), GravityType]
MagickSetImageGreenPrimary = _lib.MagickSetImageGreenPrimary
MagickSetImageGreenPrimary.restype = MagickBooleanType
MagickSetImageGreenPrimary.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickSetImageInterlaceScheme = _lib.MagickSetImageInterlaceScheme
MagickSetImageInterlaceScheme.restype = MagickBooleanType
MagickSetImageInterlaceScheme.argtypes = [POINTER(MagickWand), InterlaceType]
MagickSetImageInterpolateMethod = _lib.MagickSetImageInterpolateMethod
MagickSetImageInterpolateMethod.restype = MagickBooleanType
MagickSetImageInterpolateMethod.argtypes = [POINTER(MagickWand), InterpolatePixelMethod]
MagickSetImageIterations = _lib.MagickSetImageIterations
MagickSetImageIterations.restype = MagickBooleanType
MagickSetImageIterations.argtypes = [POINTER(MagickWand), size_t]
MagickSetImageMatte = _lib.MagickSetImageMatte
MagickSetImageMatte.restype = MagickBooleanType
MagickSetImageMatte.argtypes = [POINTER(MagickWand), MagickBooleanType]
MagickSetImageMatteColor = _lib.MagickSetImageMatteColor
MagickSetImageMatteColor.restype = MagickBooleanType
MagickSetImageMatteColor.argtypes = [POINTER(MagickWand), POINTER(PixelWand)]
MagickSetImageOpacity = _lib.MagickSetImageOpacity
MagickSetImageOpacity.restype = MagickBooleanType
MagickSetImageOpacity.argtypes = [POINTER(MagickWand), c_double]
MagickSetImageOrientation = _lib.MagickSetImageOrientation
MagickSetImageOrientation.restype = MagickBooleanType
MagickSetImageOrientation.argtypes = [POINTER(MagickWand), OrientationType]
MagickSetImagePage = _lib.MagickSetImagePage
MagickSetImagePage.restype = MagickBooleanType
MagickSetImagePage.argtypes = [POINTER(MagickWand), size_t, size_t, ssize_t, ssize_t]
MagickSetImageRedPrimary = _lib.MagickSetImageRedPrimary
MagickSetImageRedPrimary.restype = MagickBooleanType
MagickSetImageRedPrimary.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickSetImageRenderingIntent = _lib.MagickSetImageRenderingIntent
MagickSetImageRenderingIntent.restype = MagickBooleanType
MagickSetImageRenderingIntent.argtypes = [POINTER(MagickWand), RenderingIntent]
MagickSetImageResolution = _lib.MagickSetImageResolution
MagickSetImageResolution.restype = MagickBooleanType
MagickSetImageResolution.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickSetImageScene = _lib.MagickSetImageScene
MagickSetImageScene.restype = MagickBooleanType
MagickSetImageScene.argtypes = [POINTER(MagickWand), size_t]
MagickSetImageTicksPerSecond = _lib.MagickSetImageTicksPerSecond
MagickSetImageTicksPerSecond.restype = MagickBooleanType
MagickSetImageTicksPerSecond.argtypes = [POINTER(MagickWand), ssize_t]
MagickSetImageType = _lib.MagickSetImageType
MagickSetImageType.restype = MagickBooleanType
MagickSetImageType.argtypes = [POINTER(MagickWand), ImageType]
MagickSetImageUnits = _lib.MagickSetImageUnits
MagickSetImageUnits.restype = MagickBooleanType
MagickSetImageUnits.argtypes = [POINTER(MagickWand), ResolutionType]
MagickSetImageWhitePoint = _lib.MagickSetImageWhitePoint
MagickSetImageWhitePoint.restype = MagickBooleanType
MagickSetImageWhitePoint.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickShadeImage = _lib.MagickShadeImage
MagickShadeImage.restype = MagickBooleanType
MagickShadeImage.argtypes = [POINTER(MagickWand), MagickBooleanType, c_double, c_double]
MagickShadowImage = _lib.MagickShadowImage
MagickShadowImage.restype = MagickBooleanType
MagickShadowImage.argtypes = [POINTER(MagickWand), c_double, c_double, ssize_t, ssize_t]
MagickSharpenImage = _lib.MagickSharpenImage
MagickSharpenImage.restype = MagickBooleanType
MagickSharpenImage.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickSharpenImageChannel = _lib.MagickSharpenImageChannel
MagickSharpenImageChannel.restype = MagickBooleanType
MagickSharpenImageChannel.argtypes = [POINTER(MagickWand), ChannelType, c_double, c_double]
MagickShaveImage = _lib.MagickShaveImage
MagickShaveImage.restype = MagickBooleanType
MagickShaveImage.argtypes = [POINTER(MagickWand), size_t, size_t]
MagickShearImage = _lib.MagickShearImage
MagickShearImage.restype = MagickBooleanType
MagickShearImage.argtypes = [POINTER(MagickWand), POINTER(PixelWand), c_double, c_double]
MagickSigmoidalContrastImage = _lib.MagickSigmoidalContrastImage
MagickSigmoidalContrastImage.restype = MagickBooleanType
MagickSigmoidalContrastImage.argtypes = [POINTER(MagickWand), MagickBooleanType, c_double, c_double]
MagickSigmoidalContrastImageChannel = _lib.MagickSigmoidalContrastImageChannel
MagickSigmoidalContrastImageChannel.restype = MagickBooleanType
MagickSigmoidalContrastImageChannel.argtypes = [POINTER(MagickWand), ChannelType, MagickBooleanType, c_double, c_double]
MagickSketchImage = _lib.MagickSketchImage
MagickSketchImage.restype = MagickBooleanType
MagickSketchImage.argtypes = [POINTER(MagickWand), c_double, c_double, c_double]
MagickSolarizeImage = _lib.MagickSolarizeImage
MagickSolarizeImage.restype = MagickBooleanType
MagickSolarizeImage.argtypes = [POINTER(MagickWand), c_double]
MagickSparseColorImage = _lib.MagickSparseColorImage
MagickSparseColorImage.restype = MagickBooleanType
MagickSparseColorImage.argtypes = [POINTER(MagickWand), ChannelType, SparseColorMethod, size_t, POINTER(c_double)]
MagickSpliceImage = _lib.MagickSpliceImage
MagickSpliceImage.restype = MagickBooleanType
MagickSpliceImage.argtypes = [POINTER(MagickWand), size_t, size_t, ssize_t, ssize_t]
MagickSpreadImage = _lib.MagickSpreadImage
MagickSpreadImage.restype = MagickBooleanType
MagickSpreadImage.argtypes = [POINTER(MagickWand), c_double]
MagickStripImage = _lib.MagickStripImage
MagickStripImage.restype = MagickBooleanType
MagickStripImage.argtypes = [POINTER(MagickWand)]
MagickSwirlImage = _lib.MagickSwirlImage
MagickSwirlImage.restype = MagickBooleanType
MagickSwirlImage.argtypes = [POINTER(MagickWand), c_double]
MagickTintImage = _lib.MagickTintImage
MagickTintImage.restype = MagickBooleanType
MagickTintImage.argtypes = [POINTER(MagickWand), POINTER(PixelWand), POINTER(PixelWand)]
MagickTransformImageColorspace = _lib.MagickTransformImageColorspace
MagickTransformImageColorspace.restype = MagickBooleanType
MagickTransformImageColorspace.argtypes = [POINTER(MagickWand), ColorspaceType]
MagickTransposeImage = _lib.MagickTransposeImage
MagickTransposeImage.restype = MagickBooleanType
MagickTransposeImage.argtypes = [POINTER(MagickWand)]
MagickTransverseImage = _lib.MagickTransverseImage
MagickTransverseImage.restype = MagickBooleanType
MagickTransverseImage.argtypes = [POINTER(MagickWand)]
MagickThresholdImage = _lib.MagickThresholdImage
MagickThresholdImage.restype = MagickBooleanType
MagickThresholdImage.argtypes = [POINTER(MagickWand), c_double]
MagickThresholdImageChannel = _lib.MagickThresholdImageChannel
MagickThresholdImageChannel.restype = MagickBooleanType
MagickThresholdImageChannel.argtypes = [POINTER(MagickWand), ChannelType, c_double]
MagickThumbnailImage = _lib.MagickThumbnailImage
MagickThumbnailImage.restype = MagickBooleanType
MagickThumbnailImage.argtypes = [POINTER(MagickWand), size_t, size_t]
MagickTrimImage = _lib.MagickTrimImage
MagickTrimImage.restype = MagickBooleanType
MagickTrimImage.argtypes = [POINTER(MagickWand), c_double]
MagickUniqueImageColors = _lib.MagickUniqueImageColors
MagickUniqueImageColors.restype = MagickBooleanType
MagickUniqueImageColors.argtypes = [POINTER(MagickWand)]
MagickUnsharpMaskImage = _lib.MagickUnsharpMaskImage
MagickUnsharpMaskImage.restype = MagickBooleanType
MagickUnsharpMaskImage.argtypes = [POINTER(MagickWand), c_double, c_double, c_double, c_double]
MagickUnsharpMaskImageChannel = _lib.MagickUnsharpMaskImageChannel
MagickUnsharpMaskImageChannel.restype = MagickBooleanType
MagickUnsharpMaskImageChannel.argtypes = [POINTER(MagickWand), ChannelType, c_double, c_double, c_double, c_double]
MagickVignetteImage = _lib.MagickVignetteImage
MagickVignetteImage.restype = MagickBooleanType
MagickVignetteImage.argtypes = [POINTER(MagickWand), c_double, c_double, ssize_t, ssize_t]
MagickWaveImage = _lib.MagickWaveImage
MagickWaveImage.restype = MagickBooleanType
MagickWaveImage.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickWhiteThresholdImage = _lib.MagickWhiteThresholdImage
MagickWhiteThresholdImage.restype = MagickBooleanType
MagickWhiteThresholdImage.argtypes = [POINTER(MagickWand), POINTER(PixelWand)]
MagickWriteImage = _lib.MagickWriteImage
MagickWriteImage.restype = MagickBooleanType
MagickWriteImage.argtypes = [POINTER(MagickWand), STRING]
MagickWriteImageFile = _lib.MagickWriteImageFile
MagickWriteImageFile.restype = MagickBooleanType
MagickWriteImageFile.argtypes = [POINTER(MagickWand), POINTER(FILE)]
MagickWriteImages = _lib.MagickWriteImages
MagickWriteImages.restype = MagickBooleanType
MagickWriteImages.argtypes = [POINTER(MagickWand), STRING, MagickBooleanType]
MagickWriteImagesFile = _lib.MagickWriteImagesFile
MagickWriteImagesFile.restype = MagickBooleanType
MagickWriteImagesFile.argtypes = [POINTER(MagickWand), POINTER(FILE)]
MagickSetImageProgressMonitor = _lib.MagickSetImageProgressMonitor
MagickSetImageProgressMonitor.restype = MagickProgressMonitor
MagickSetImageProgressMonitor.argtypes = [POINTER(MagickWand), MagickProgressMonitor, c_void_p]
MagickAppendImages = _lib.MagickAppendImages
MagickAppendImages.restype = POINTER(MagickWand)
MagickAppendImages.argtypes = [POINTER(MagickWand), MagickBooleanType]
MagickCoalesceImages = _lib.MagickCoalesceImages
MagickCoalesceImages.restype = POINTER(MagickWand)
MagickCoalesceImages.argtypes = [POINTER(MagickWand)]
MagickCombineImages = _lib.MagickCombineImages
MagickCombineImages.restype = POINTER(MagickWand)
MagickCombineImages.argtypes = [POINTER(MagickWand), ChannelType]
MagickCompareImageChannels = _lib.MagickCompareImageChannels
MagickCompareImageChannels.restype = POINTER(MagickWand)
MagickCompareImageChannels.argtypes = [POINTER(MagickWand), POINTER(MagickWand), ChannelType, MetricType, POINTER(c_double)]
MagickCompareImages = _lib.MagickCompareImages
MagickCompareImages.restype = POINTER(MagickWand)
MagickCompareImages.argtypes = [POINTER(MagickWand), POINTER(MagickWand), MetricType, POINTER(c_double)]
MagickCompareImageLayers = _lib.MagickCompareImageLayers
MagickCompareImageLayers.restype = POINTER(MagickWand)
MagickCompareImageLayers.argtypes = [POINTER(MagickWand), ImageLayerMethod]
MagickDeconstructImages = _lib.MagickDeconstructImages
MagickDeconstructImages.restype = POINTER(MagickWand)
MagickDeconstructImages.argtypes = [POINTER(MagickWand)]
MagickEvaluateImages = _lib.MagickEvaluateImages
MagickEvaluateImages.restype = POINTER(MagickWand)
MagickEvaluateImages.argtypes = [POINTER(MagickWand), MagickEvaluateOperator]
MagickFxImage = _lib.MagickFxImage
MagickFxImage.restype = POINTER(MagickWand)
MagickFxImage.argtypes = [POINTER(MagickWand), STRING]
MagickFxImageChannel = _lib.MagickFxImageChannel
MagickFxImageChannel.restype = POINTER(MagickWand)
MagickFxImageChannel.argtypes = [POINTER(MagickWand), ChannelType, STRING]
MagickGetImage = _lib.MagickGetImage
MagickGetImage.restype = POINTER(MagickWand)
MagickGetImage.argtypes = [POINTER(MagickWand)]
MagickGetImageClipMask = _lib.MagickGetImageClipMask
MagickGetImageClipMask.restype = POINTER(MagickWand)
MagickGetImageClipMask.argtypes = [POINTER(MagickWand)]
MagickGetImageRegion = _lib.MagickGetImageRegion
MagickGetImageRegion.restype = POINTER(MagickWand)
MagickGetImageRegion.argtypes = [POINTER(MagickWand), size_t, size_t, ssize_t, ssize_t]
MagickMergeImageLayers = _lib.MagickMergeImageLayers
MagickMergeImageLayers.restype = POINTER(MagickWand)
MagickMergeImageLayers.argtypes = [POINTER(MagickWand), ImageLayerMethod]
MagickMorphImages = _lib.MagickMorphImages
MagickMorphImages.restype = POINTER(MagickWand)
MagickMorphImages.argtypes = [POINTER(MagickWand), size_t]
MagickMontageImage = _lib.MagickMontageImage
MagickMontageImage.restype = POINTER(MagickWand)
MagickMontageImage.argtypes = [POINTER(MagickWand), POINTER(DrawingWand), STRING, STRING, MontageMode, STRING]
MagickOptimizeImageLayers = _lib.MagickOptimizeImageLayers
MagickOptimizeImageLayers.restype = POINTER(MagickWand)
MagickOptimizeImageLayers.argtypes = [POINTER(MagickWand)]
MagickPreviewImages = _lib.MagickPreviewImages
MagickPreviewImages.restype = POINTER(MagickWand)
MagickPreviewImages.argtypes = [POINTER(MagickWand), PreviewType]
MagickSimilarityImage = _lib.MagickSimilarityImage
MagickSimilarityImage.restype = POINTER(MagickWand)
MagickSimilarityImage.argtypes = [POINTER(MagickWand), POINTER(MagickWand), POINTER(RectangleInfo), POINTER(c_double)]
MagickSteganoImage = _lib.MagickSteganoImage
MagickSteganoImage.restype = POINTER(MagickWand)
MagickSteganoImage.argtypes = [POINTER(MagickWand), POINTER(MagickWand), ssize_t]
MagickStereoImage = _lib.MagickStereoImage
MagickStereoImage.restype = POINTER(MagickWand)
MagickStereoImage.argtypes = [POINTER(MagickWand), POINTER(MagickWand)]
MagickTextureImage = _lib.MagickTextureImage
MagickTextureImage.restype = POINTER(MagickWand)
MagickTextureImage.argtypes = [POINTER(MagickWand), POINTER(MagickWand)]
MagickTransformImage = _lib.MagickTransformImage
MagickTransformImage.restype = POINTER(MagickWand)
MagickTransformImage.argtypes = [POINTER(MagickWand), STRING, STRING]
MagickGetImageOrientation = _lib.MagickGetImageOrientation
MagickGetImageOrientation.restype = OrientationType
MagickGetImageOrientation.argtypes = [POINTER(MagickWand)]
MagickGetImageHistogram = _lib.MagickGetImageHistogram
MagickGetImageHistogram.restype = POINTER(POINTER(PixelWand))
MagickGetImageHistogram.argtypes = [POINTER(MagickWand), POINTER(size_t)]
MagickGetImageRenderingIntent = _lib.MagickGetImageRenderingIntent
MagickGetImageRenderingIntent.restype = RenderingIntent
MagickGetImageRenderingIntent.argtypes = [POINTER(MagickWand)]
MagickGetImageUnits = _lib.MagickGetImageUnits
MagickGetImageUnits.restype = ResolutionType
MagickGetImageUnits.argtypes = [POINTER(MagickWand)]
MagickGetImageColors = _lib.MagickGetImageColors
MagickGetImageColors.restype = size_t
MagickGetImageColors.argtypes = [POINTER(MagickWand)]
MagickGetImageCompressionQuality = _lib.MagickGetImageCompressionQuality
MagickGetImageCompressionQuality.restype = size_t
MagickGetImageCompressionQuality.argtypes = [POINTER(MagickWand)]
MagickGetImageDelay = _lib.MagickGetImageDelay
MagickGetImageDelay.restype = size_t
MagickGetImageDelay.argtypes = [POINTER(MagickWand)]
MagickGetImageChannelDepth = _lib.MagickGetImageChannelDepth
MagickGetImageChannelDepth.restype = size_t
MagickGetImageChannelDepth.argtypes = [POINTER(MagickWand), ChannelType]
MagickGetImageDepth = _lib.MagickGetImageDepth
MagickGetImageDepth.restype = size_t
MagickGetImageDepth.argtypes = [POINTER(MagickWand)]
MagickGetImageHeight = _lib.MagickGetImageHeight
MagickGetImageHeight.restype = size_t
MagickGetImageHeight.argtypes = [POINTER(MagickWand)]
MagickGetImageIterations = _lib.MagickGetImageIterations
MagickGetImageIterations.restype = size_t
MagickGetImageIterations.argtypes = [POINTER(MagickWand)]
MagickGetImageScene = _lib.MagickGetImageScene
MagickGetImageScene.restype = size_t
MagickGetImageScene.argtypes = [POINTER(MagickWand)]
MagickGetImageTicksPerSecond = _lib.MagickGetImageTicksPerSecond
MagickGetImageTicksPerSecond.restype = size_t
MagickGetImageTicksPerSecond.argtypes = [POINTER(MagickWand)]
MagickGetImageWidth = _lib.MagickGetImageWidth
MagickGetImageWidth.restype = size_t
MagickGetImageWidth.argtypes = [POINTER(MagickWand)]
MagickGetNumberImages = _lib.MagickGetNumberImages
MagickGetNumberImages.restype = size_t
MagickGetNumberImages.argtypes = [POINTER(MagickWand)]
MagickGetImageBlob = _lib.MagickGetImageBlob
MagickGetImageBlob.restype = POINTER(c_ubyte)
MagickGetImageBlob.argtypes = [POINTER(MagickWand), POINTER(size_t)]
MagickGetImagesBlob = _lib.MagickGetImagesBlob
MagickGetImagesBlob.restype = POINTER(c_ubyte)
MagickGetImagesBlob.argtypes = [POINTER(MagickWand), POINTER(size_t)]
MagickGetImageVirtualPixelMethod = _lib.MagickGetImageVirtualPixelMethod
MagickGetImageVirtualPixelMethod.restype = VirtualPixelMethod
MagickGetImageVirtualPixelMethod.argtypes = [POINTER(MagickWand)]
MagickSetImageVirtualPixelMethod = _lib.MagickSetImageVirtualPixelMethod
MagickSetImageVirtualPixelMethod.restype = VirtualPixelMethod
MagickSetImageVirtualPixelMethod.argtypes = [POINTER(MagickWand), VirtualPixelMethod]
MagickGetFilename = _lib.MagickGetFilename
MagickGetFilename.restype = STRING
MagickGetFilename.argtypes = [POINTER(MagickWand)]
MagickGetFormat = _lib.MagickGetFormat
MagickGetFormat.restype = STRING
MagickGetFormat.argtypes = [POINTER(MagickWand)]
MagickGetFont = _lib.MagickGetFont
MagickGetFont.restype = STRING
MagickGetFont.argtypes = [POINTER(MagickWand)]
MagickGetHomeURL = _lib.MagickGetHomeURL
MagickGetHomeURL.restype = STRING
MagickGetHomeURL.argtypes = []
MagickGetImageArtifact = _lib.MagickGetImageArtifact
MagickGetImageArtifact.restype = STRING
MagickGetImageArtifact.argtypes = [POINTER(MagickWand), STRING]
MagickGetImageArtifacts = _lib.MagickGetImageArtifacts
MagickGetImageArtifacts.restype = POINTER(STRING)
MagickGetImageArtifacts.argtypes = [POINTER(MagickWand), STRING, POINTER(size_t)]
MagickGetImageProfiles = _lib.MagickGetImageProfiles
MagickGetImageProfiles.restype = POINTER(STRING)
MagickGetImageProfiles.argtypes = [POINTER(MagickWand), STRING, POINTER(size_t)]
MagickGetImageProperty = _lib.MagickGetImageProperty
MagickGetImageProperty.restype = STRING
MagickGetImageProperty.argtypes = [POINTER(MagickWand), STRING]
MagickGetImageProperties = _lib.MagickGetImageProperties
MagickGetImageProperties.restype = POINTER(STRING)
MagickGetImageProperties.argtypes = [POINTER(MagickWand), STRING, POINTER(size_t)]
MagickGetOption = _lib.MagickGetOption
MagickGetOption.restype = STRING
MagickGetOption.argtypes = [POINTER(MagickWand), STRING]
MagickGetOptions = _lib.MagickGetOptions
MagickGetOptions.restype = POINTER(STRING)
MagickGetOptions.argtypes = [POINTER(MagickWand), STRING, POINTER(size_t)]
MagickQueryConfigureOption = _lib.MagickQueryConfigureOption
MagickQueryConfigureOption.restype = STRING
MagickQueryConfigureOption.argtypes = [STRING]
MagickQueryConfigureOptions = _lib.MagickQueryConfigureOptions
MagickQueryConfigureOptions.restype = POINTER(STRING)
MagickQueryConfigureOptions.argtypes = [STRING, POINTER(size_t)]
MagickQueryFonts = _lib.MagickQueryFonts
MagickQueryFonts.restype = POINTER(STRING)
MagickQueryFonts.argtypes = [STRING, POINTER(size_t)]
MagickQueryFormats = _lib.MagickQueryFormats
MagickQueryFormats.restype = POINTER(STRING)
MagickQueryFormats.argtypes = [STRING, POINTER(size_t)]
MagickGetColorspace = _lib.MagickGetColorspace
MagickGetColorspace.restype = ColorspaceType
MagickGetColorspace.argtypes = [POINTER(MagickWand)]
MagickGetCompression = _lib.MagickGetCompression
MagickGetCompression.restype = CompressionType
MagickGetCompression.argtypes = [POINTER(MagickWand)]
MagickGetCopyright = _lib.MagickGetCopyright
MagickGetCopyright.restype = STRING
MagickGetCopyright.argtypes = []
MagickGetPackageName = _lib.MagickGetPackageName
MagickGetPackageName.restype = STRING
MagickGetPackageName.argtypes = []
MagickGetQuantumDepth = _lib.MagickGetQuantumDepth
MagickGetQuantumDepth.restype = STRING
MagickGetQuantumDepth.argtypes = [POINTER(size_t)]
MagickGetQuantumRange = _lib.MagickGetQuantumRange
MagickGetQuantumRange.restype = STRING
MagickGetQuantumRange.argtypes = [POINTER(size_t)]
MagickGetReleaseDate = _lib.MagickGetReleaseDate
MagickGetReleaseDate.restype = STRING
MagickGetReleaseDate.argtypes = []
MagickGetVersion = _lib.MagickGetVersion
MagickGetVersion.restype = STRING
MagickGetVersion.argtypes = [POINTER(size_t)]
MagickGetPointsize = _lib.MagickGetPointsize
MagickGetPointsize.restype = c_double
MagickGetPointsize.argtypes = [POINTER(MagickWand)]
MagickGetSamplingFactors = _lib.MagickGetSamplingFactors
MagickGetSamplingFactors.restype = POINTER(c_double)
MagickGetSamplingFactors.argtypes = [POINTER(MagickWand), POINTER(size_t)]
MagickQueryFontMetrics = _lib.MagickQueryFontMetrics
MagickQueryFontMetrics.restype = POINTER(c_double)
MagickQueryFontMetrics.argtypes = [POINTER(MagickWand), POINTER(DrawingWand), STRING]
MagickQueryMultilineFontMetrics = _lib.MagickQueryMultilineFontMetrics
MagickQueryMultilineFontMetrics.restype = POINTER(c_double)
MagickQueryMultilineFontMetrics.argtypes = [POINTER(MagickWand), POINTER(DrawingWand), STRING]
MagickGetGravity = _lib.MagickGetGravity
MagickGetGravity.restype = GravityType
MagickGetGravity.argtypes = [POINTER(MagickWand)]
MagickGetType = _lib.MagickGetType
MagickGetType.restype = ImageType
MagickGetType.argtypes = [POINTER(MagickWand)]
MagickGetInterlaceScheme = _lib.MagickGetInterlaceScheme
MagickGetInterlaceScheme.restype = InterlaceType
MagickGetInterlaceScheme.argtypes = [POINTER(MagickWand)]
MagickGetInterpolateMethod = _lib.MagickGetInterpolateMethod
MagickGetInterpolateMethod.restype = InterpolatePixelMethod
MagickGetInterpolateMethod.argtypes = [POINTER(MagickWand)]
MagickGetOrientation = _lib.MagickGetOrientation
MagickGetOrientation.restype = OrientationType
MagickGetOrientation.argtypes = [POINTER(MagickWand)]
MagickDeleteImageArtifact = _lib.MagickDeleteImageArtifact
MagickDeleteImageArtifact.restype = MagickBooleanType
MagickDeleteImageArtifact.argtypes = [POINTER(MagickWand), STRING]
MagickDeleteImageProperty = _lib.MagickDeleteImageProperty
MagickDeleteImageProperty.restype = MagickBooleanType
MagickDeleteImageProperty.argtypes = [POINTER(MagickWand), STRING]
MagickDeleteOption = _lib.MagickDeleteOption
MagickDeleteOption.restype = MagickBooleanType
MagickDeleteOption.argtypes = [POINTER(MagickWand), STRING]
MagickGetAntialias = _lib.MagickGetAntialias
MagickGetAntialias.restype = MagickBooleanType
MagickGetAntialias.argtypes = [POINTER(MagickWand)]
MagickGetPage = _lib.MagickGetPage
MagickGetPage.restype = MagickBooleanType
MagickGetPage.argtypes = [POINTER(MagickWand), POINTER(size_t), POINTER(size_t), POINTER(ssize_t), POINTER(ssize_t)]
MagickGetSize = _lib.MagickGetSize
MagickGetSize.restype = MagickBooleanType
MagickGetSize.argtypes = [POINTER(MagickWand), POINTER(size_t), POINTER(size_t)]
MagickGetSizeOffset = _lib.MagickGetSizeOffset
MagickGetSizeOffset.restype = MagickBooleanType
MagickGetSizeOffset.argtypes = [POINTER(MagickWand), POINTER(ssize_t)]
MagickProfileImage = _lib.MagickProfileImage
MagickProfileImage.restype = MagickBooleanType
MagickProfileImage.argtypes = [POINTER(MagickWand), STRING, c_void_p, size_t]
MagickSetAntialias = _lib.MagickSetAntialias
MagickSetAntialias.restype = MagickBooleanType
MagickSetAntialias.argtypes = [POINTER(MagickWand), MagickBooleanType]
MagickSetBackgroundColor = _lib.MagickSetBackgroundColor
MagickSetBackgroundColor.restype = MagickBooleanType
MagickSetBackgroundColor.argtypes = [POINTER(MagickWand), POINTER(PixelWand)]
MagickSetColorspace = _lib.MagickSetColorspace
MagickSetColorspace.restype = MagickBooleanType
MagickSetColorspace.argtypes = [POINTER(MagickWand), ColorspaceType]
MagickSetCompression = _lib.MagickSetCompression
MagickSetCompression.restype = MagickBooleanType
MagickSetCompression.argtypes = [POINTER(MagickWand), CompressionType]
MagickSetCompressionQuality = _lib.MagickSetCompressionQuality
MagickSetCompressionQuality.restype = MagickBooleanType
MagickSetCompressionQuality.argtypes = [POINTER(MagickWand), size_t]
MagickSetDepth = _lib.MagickSetDepth
MagickSetDepth.restype = MagickBooleanType
MagickSetDepth.argtypes = [POINTER(MagickWand), size_t]
MagickSetExtract = _lib.MagickSetExtract
MagickSetExtract.restype = MagickBooleanType
MagickSetExtract.argtypes = [POINTER(MagickWand), STRING]
MagickSetFilename = _lib.MagickSetFilename
MagickSetFilename.restype = MagickBooleanType
MagickSetFilename.argtypes = [POINTER(MagickWand), STRING]
MagickSetFormat = _lib.MagickSetFormat
MagickSetFormat.restype = MagickBooleanType
MagickSetFormat.argtypes = [POINTER(MagickWand), STRING]
MagickSetFont = _lib.MagickSetFont
MagickSetFont.restype = MagickBooleanType
MagickSetFont.argtypes = [POINTER(MagickWand), STRING]
MagickSetGravity = _lib.MagickSetGravity
MagickSetGravity.restype = MagickBooleanType
MagickSetGravity.argtypes = [POINTER(MagickWand), GravityType]
MagickSetImageArtifact = _lib.MagickSetImageArtifact
MagickSetImageArtifact.restype = MagickBooleanType
MagickSetImageArtifact.argtypes = [POINTER(MagickWand), STRING, STRING]
MagickSetImageProfile = _lib.MagickSetImageProfile
MagickSetImageProfile.restype = MagickBooleanType
MagickSetImageProfile.argtypes = [POINTER(MagickWand), STRING, c_void_p, size_t]
MagickSetImageProperty = _lib.MagickSetImageProperty
MagickSetImageProperty.restype = MagickBooleanType
MagickSetImageProperty.argtypes = [POINTER(MagickWand), STRING, STRING]
MagickSetInterlaceScheme = _lib.MagickSetInterlaceScheme
MagickSetInterlaceScheme.restype = MagickBooleanType
MagickSetInterlaceScheme.argtypes = [POINTER(MagickWand), InterlaceType]
MagickSetInterpolateMethod = _lib.MagickSetInterpolateMethod
MagickSetInterpolateMethod.restype = MagickBooleanType
MagickSetInterpolateMethod.argtypes = [POINTER(MagickWand), InterpolatePixelMethod]
MagickSetOption = _lib.MagickSetOption
MagickSetOption.restype = MagickBooleanType
MagickSetOption.argtypes = [POINTER(MagickWand), STRING, STRING]
MagickSetOrientation = _lib.MagickSetOrientation
MagickSetOrientation.restype = MagickBooleanType
MagickSetOrientation.argtypes = [POINTER(MagickWand), OrientationType]
MagickSetPage = _lib.MagickSetPage
MagickSetPage.restype = MagickBooleanType
MagickSetPage.argtypes = [POINTER(MagickWand), size_t, size_t, ssize_t, ssize_t]
MagickSetPassphrase = _lib.MagickSetPassphrase
MagickSetPassphrase.restype = MagickBooleanType
MagickSetPassphrase.argtypes = [POINTER(MagickWand), STRING]
MagickSetPointsize = _lib.MagickSetPointsize
MagickSetPointsize.restype = MagickBooleanType
MagickSetPointsize.argtypes = [POINTER(MagickWand), c_double]
MagickSetResolution = _lib.MagickSetResolution
MagickSetResolution.restype = MagickBooleanType
MagickSetResolution.argtypes = [POINTER(MagickWand), c_double, c_double]
MagickSetResourceLimit = _lib.MagickSetResourceLimit
MagickSetResourceLimit.restype = MagickBooleanType
MagickSetResourceLimit.argtypes = [ResourceType, MagickSizeType]
MagickSetSamplingFactors = _lib.MagickSetSamplingFactors
MagickSetSamplingFactors.restype = MagickBooleanType
MagickSetSamplingFactors.argtypes = [POINTER(MagickWand), size_t, POINTER(c_double)]
MagickSetSize = _lib.MagickSetSize
MagickSetSize.restype = MagickBooleanType
MagickSetSize.argtypes = [POINTER(MagickWand), size_t, size_t]
MagickSetSizeOffset = _lib.MagickSetSizeOffset
MagickSetSizeOffset.restype = MagickBooleanType
MagickSetSizeOffset.argtypes = [POINTER(MagickWand), size_t, size_t, ssize_t]
MagickSetType = _lib.MagickSetType
MagickSetType.restype = MagickBooleanType
MagickSetType.argtypes = [POINTER(MagickWand), ImageType]
MagickSetProgressMonitor = _lib.MagickSetProgressMonitor
MagickSetProgressMonitor.restype = MagickProgressMonitor
MagickSetProgressMonitor.argtypes = [POINTER(MagickWand), MagickProgressMonitor, c_void_p]
MagickGetResource = _lib.MagickGetResource
MagickGetResource.restype = MagickSizeType
MagickGetResource.argtypes = [ResourceType]
MagickGetResourceLimit = _lib.MagickGetResourceLimit
MagickGetResourceLimit.restype = MagickSizeType
MagickGetResourceLimit.argtypes = [ResourceType]
MagickGetBackgroundColor = _lib.MagickGetBackgroundColor
MagickGetBackgroundColor.restype = POINTER(PixelWand)
MagickGetBackgroundColor.argtypes = [POINTER(MagickWand)]
MagickGetCompressionQuality = _lib.MagickGetCompressionQuality
MagickGetCompressionQuality.restype = size_t
MagickGetCompressionQuality.argtypes = [POINTER(MagickWand)]
MagickGetImageProfile = _lib.MagickGetImageProfile
MagickGetImageProfile.restype = POINTER(c_ubyte)
MagickGetImageProfile.argtypes = [POINTER(MagickWand), STRING, POINTER(size_t)]
MagickRemoveImageProfile = _lib.MagickRemoveImageProfile
MagickRemoveImageProfile.restype = POINTER(c_ubyte)
MagickRemoveImageProfile.argtypes = [POINTER(MagickWand), STRING, POINTER(size_t)]
MagickCommand = CFUNCTYPE(MagickBooleanType, POINTER(ImageInfo), c_int, POINTER(STRING), POINTER(STRING), POINTER(ExceptionInfo))
MagickCommandGenesis = _lib.MagickCommandGenesis
MagickCommandGenesis.restype = MagickBooleanType
MagickCommandGenesis.argtypes = [POINTER(ImageInfo), MagickCommand, c_int, POINTER(STRING), POINTER(STRING), POINTER(ExceptionInfo)]
MogrifyImage = _lib.MogrifyImage
MogrifyImage.restype = MagickBooleanType
MogrifyImage.argtypes = [POINTER(ImageInfo), c_int, POINTER(STRING), POINTER(POINTER(Image)), POINTER(ExceptionInfo)]
MogrifyImageCommand = _lib.MogrifyImageCommand
MogrifyImageCommand.restype = MagickBooleanType
MogrifyImageCommand.argtypes = [POINTER(ImageInfo), c_int, POINTER(STRING), POINTER(STRING), POINTER(ExceptionInfo)]
MogrifyImageInfo = _lib.MogrifyImageInfo
MogrifyImageInfo.restype = MagickBooleanType
MogrifyImageInfo.argtypes = [POINTER(ImageInfo), c_int, POINTER(STRING), POINTER(ExceptionInfo)]
MogrifyImageList = _lib.MogrifyImageList
MogrifyImageList.restype = MagickBooleanType
MogrifyImageList.argtypes = [POINTER(ImageInfo), c_int, POINTER(STRING), POINTER(POINTER(Image)), POINTER(ExceptionInfo)]
MogrifyImages = _lib.MogrifyImages
MogrifyImages.restype = MagickBooleanType
MogrifyImages.argtypes = [POINTER(ImageInfo), MagickBooleanType, c_int, POINTER(STRING), POINTER(POINTER(Image)), POINTER(ExceptionInfo)]
MontageImageCommand = _lib.MontageImageCommand
MontageImageCommand.restype = MagickBooleanType
MontageImageCommand.argtypes = [POINTER(ImageInfo), c_int, POINTER(STRING), POINTER(STRING), POINTER(ExceptionInfo)]
PixelGetIteratorException = _lib.PixelGetIteratorException
PixelGetIteratorException.restype = STRING
PixelGetIteratorException.argtypes = [POINTER(PixelIterator), POINTER(ExceptionType)]
PixelGetIteratorExceptionType = _lib.PixelGetIteratorExceptionType
PixelGetIteratorExceptionType.restype = ExceptionType
PixelGetIteratorExceptionType.argtypes = [POINTER(PixelIterator)]
IsPixelIterator = _lib.IsPixelIterator
IsPixelIterator.restype = MagickBooleanType
IsPixelIterator.argtypes = [POINTER(PixelIterator)]
PixelClearIteratorException = _lib.PixelClearIteratorException
PixelClearIteratorException.restype = MagickBooleanType
PixelClearIteratorException.argtypes = [POINTER(PixelIterator)]
PixelSetIteratorRow = _lib.PixelSetIteratorRow
PixelSetIteratorRow.restype = MagickBooleanType
PixelSetIteratorRow.argtypes = [POINTER(PixelIterator), ssize_t]
PixelSyncIterator = _lib.PixelSyncIterator
PixelSyncIterator.restype = MagickBooleanType
PixelSyncIterator.argtypes = [POINTER(PixelIterator)]
ClonePixelIterator = _lib.ClonePixelIterator
ClonePixelIterator.restype = POINTER(PixelIterator)
ClonePixelIterator.argtypes = [POINTER(PixelIterator)]
DestroyPixelIterator = _lib.DestroyPixelIterator
DestroyPixelIterator.restype = POINTER(PixelIterator)
DestroyPixelIterator.argtypes = [POINTER(PixelIterator)]
NewPixelIterator = _lib.NewPixelIterator
NewPixelIterator.restype = POINTER(PixelIterator)
NewPixelIterator.argtypes = [POINTER(MagickWand)]
NewPixelRegionIterator = _lib.NewPixelRegionIterator
NewPixelRegionIterator.restype = POINTER(PixelIterator)
NewPixelRegionIterator.argtypes = [POINTER(MagickWand), ssize_t, ssize_t, size_t, size_t]
PixelGetCurrentIteratorRow = _lib.PixelGetCurrentIteratorRow
PixelGetCurrentIteratorRow.restype = POINTER(POINTER(PixelWand))
PixelGetCurrentIteratorRow.argtypes = [POINTER(PixelIterator), POINTER(size_t)]
PixelGetNextIteratorRow = _lib.PixelGetNextIteratorRow
PixelGetNextIteratorRow.restype = POINTER(POINTER(PixelWand))
PixelGetNextIteratorRow.argtypes = [POINTER(PixelIterator), POINTER(size_t)]
PixelGetPreviousIteratorRow = _lib.PixelGetPreviousIteratorRow
PixelGetPreviousIteratorRow.restype = POINTER(POINTER(PixelWand))
PixelGetPreviousIteratorRow.argtypes = [POINTER(PixelIterator), POINTER(size_t)]
PixelGetIteratorRow = _lib.PixelGetIteratorRow
PixelGetIteratorRow.restype = ssize_t
PixelGetIteratorRow.argtypes = [POINTER(PixelIterator)]
ClearPixelIterator = _lib.ClearPixelIterator
ClearPixelIterator.restype = None
ClearPixelIterator.argtypes = [POINTER(PixelIterator)]
PixelResetIterator = _lib.PixelResetIterator
PixelResetIterator.restype = None
PixelResetIterator.argtypes = [POINTER(PixelIterator)]
PixelSetFirstIteratorRow = _lib.PixelSetFirstIteratorRow
PixelSetFirstIteratorRow.restype = None
PixelSetFirstIteratorRow.argtypes = [POINTER(PixelIterator)]
PixelSetLastIteratorRow = _lib.PixelSetLastIteratorRow
PixelSetLastIteratorRow.restype = None
PixelSetLastIteratorRow.argtypes = [POINTER(PixelIterator)]
class _PixelView(Structure):
    pass
PixelView = _PixelView
DuplexTransferPixelViewMethod = CFUNCTYPE(MagickBooleanType, POINTER(PixelView), POINTER(PixelView), POINTER(PixelView), c_void_p)
GetPixelViewMethod = CFUNCTYPE(MagickBooleanType, POINTER(PixelView), c_void_p)
SetPixelViewMethod = CFUNCTYPE(MagickBooleanType, POINTER(PixelView), c_void_p)
TransferPixelViewMethod = CFUNCTYPE(MagickBooleanType, POINTER(PixelView), POINTER(PixelView), c_void_p)
UpdatePixelViewMethod = CFUNCTYPE(MagickBooleanType, POINTER(PixelView), c_void_p)
GetPixelViewException = _lib.GetPixelViewException
GetPixelViewException.restype = STRING
GetPixelViewException.argtypes = [POINTER(PixelView), POINTER(ExceptionType)]
DuplexTransferPixelViewIterator = _lib.DuplexTransferPixelViewIterator
DuplexTransferPixelViewIterator.restype = MagickBooleanType
DuplexTransferPixelViewIterator.argtypes = [POINTER(PixelView), POINTER(PixelView), POINTER(PixelView), DuplexTransferPixelViewMethod, c_void_p]
GetPixelViewIterator = _lib.GetPixelViewIterator
GetPixelViewIterator.restype = MagickBooleanType
GetPixelViewIterator.argtypes = [POINTER(PixelView), GetPixelViewMethod, c_void_p]
IsPixelView = _lib.IsPixelView
IsPixelView.restype = MagickBooleanType
IsPixelView.argtypes = [POINTER(PixelView)]
SetPixelViewIterator = _lib.SetPixelViewIterator
SetPixelViewIterator.restype = MagickBooleanType
SetPixelViewIterator.argtypes = [POINTER(PixelView), SetPixelViewMethod, c_void_p]
TransferPixelViewIterator = _lib.TransferPixelViewIterator
TransferPixelViewIterator.restype = MagickBooleanType
TransferPixelViewIterator.argtypes = [POINTER(PixelView), POINTER(PixelView), TransferPixelViewMethod, c_void_p]
UpdatePixelViewIterator = _lib.UpdatePixelViewIterator
UpdatePixelViewIterator.restype = MagickBooleanType
UpdatePixelViewIterator.argtypes = [POINTER(PixelView), UpdatePixelViewMethod, c_void_p]
GetPixelViewWand = _lib.GetPixelViewWand
GetPixelViewWand.restype = POINTER(MagickWand)
GetPixelViewWand.argtypes = [POINTER(PixelView)]
ClonePixelView = _lib.ClonePixelView
ClonePixelView.restype = POINTER(PixelView)
ClonePixelView.argtypes = [POINTER(PixelView)]
DestroyPixelView = _lib.DestroyPixelView
DestroyPixelView.restype = POINTER(PixelView)
DestroyPixelView.argtypes = [POINTER(PixelView)]
NewPixelView = _lib.NewPixelView
NewPixelView.restype = POINTER(PixelView)
NewPixelView.argtypes = [POINTER(MagickWand)]
NewPixelViewRegion = _lib.NewPixelViewRegion
NewPixelViewRegion.restype = POINTER(PixelView)
NewPixelViewRegion.argtypes = [POINTER(MagickWand), ssize_t, ssize_t, size_t, size_t]
GetPixelViewPixels = _lib.GetPixelViewPixels
GetPixelViewPixels.restype = POINTER(POINTER(PixelWand))
GetPixelViewPixels.argtypes = [POINTER(PixelView)]
GetPixelViewHeight = _lib.GetPixelViewHeight
GetPixelViewHeight.restype = size_t
GetPixelViewHeight.argtypes = [POINTER(PixelView)]
GetPixelViewWidth = _lib.GetPixelViewWidth
GetPixelViewWidth.restype = size_t
GetPixelViewWidth.argtypes = [POINTER(PixelView)]
GetPixelViewX = _lib.GetPixelViewX
GetPixelViewX.restype = ssize_t
GetPixelViewX.argtypes = [POINTER(PixelView)]
GetPixelViewY = _lib.GetPixelViewY
GetPixelViewY.restype = ssize_t
GetPixelViewY.argtypes = [POINTER(PixelView)]
PixelGetColorAsNormalizedString = _lib.PixelGetColorAsNormalizedString
PixelGetColorAsNormalizedString.restype = STRING
PixelGetColorAsNormalizedString.argtypes = [POINTER(PixelWand)]
PixelGetColorAsString = _lib.PixelGetColorAsString
PixelGetColorAsString.restype = STRING
PixelGetColorAsString.argtypes = [POINTER(PixelWand)]
PixelGetException = _lib.PixelGetException
PixelGetException.restype = STRING
PixelGetException.argtypes = [POINTER(PixelWand), POINTER(ExceptionType)]
PixelGetAlpha = _lib.PixelGetAlpha
PixelGetAlpha.restype = c_double
PixelGetAlpha.argtypes = [POINTER(PixelWand)]
PixelGetBlack = _lib.PixelGetBlack
PixelGetBlack.restype = c_double
PixelGetBlack.argtypes = [POINTER(PixelWand)]
PixelGetBlue = _lib.PixelGetBlue
PixelGetBlue.restype = c_double
PixelGetBlue.argtypes = [POINTER(PixelWand)]
PixelGetCyan = _lib.PixelGetCyan
PixelGetCyan.restype = c_double
PixelGetCyan.argtypes = [POINTER(PixelWand)]
PixelGetFuzz = _lib.PixelGetFuzz
PixelGetFuzz.restype = c_double
PixelGetFuzz.argtypes = [POINTER(PixelWand)]
PixelGetGreen = _lib.PixelGetGreen
PixelGetGreen.restype = c_double
PixelGetGreen.argtypes = [POINTER(PixelWand)]
PixelGetMagenta = _lib.PixelGetMagenta
PixelGetMagenta.restype = c_double
PixelGetMagenta.argtypes = [POINTER(PixelWand)]
PixelGetOpacity = _lib.PixelGetOpacity
PixelGetOpacity.restype = c_double
PixelGetOpacity.argtypes = [POINTER(PixelWand)]
PixelGetRed = _lib.PixelGetRed
PixelGetRed.restype = c_double
PixelGetRed.argtypes = [POINTER(PixelWand)]
PixelGetYellow = _lib.PixelGetYellow
PixelGetYellow.restype = c_double
PixelGetYellow.argtypes = [POINTER(PixelWand)]
PixelGetExceptionType = _lib.PixelGetExceptionType
PixelGetExceptionType.restype = ExceptionType
PixelGetExceptionType.argtypes = [POINTER(PixelWand)]
PixelGetIndex = _lib.PixelGetIndex
PixelGetIndex.restype = IndexPacket
PixelGetIndex.argtypes = [POINTER(PixelWand)]
IsPixelWand = _lib.IsPixelWand
IsPixelWand.restype = MagickBooleanType
IsPixelWand.argtypes = [POINTER(PixelWand)]
IsPixelWandSimilar = _lib.IsPixelWandSimilar
IsPixelWandSimilar.restype = MagickBooleanType
IsPixelWandSimilar.argtypes = [POINTER(PixelWand), POINTER(PixelWand), c_double]
PixelClearException = _lib.PixelClearException
PixelClearException.restype = MagickBooleanType
PixelClearException.argtypes = [POINTER(PixelWand)]
PixelSetColor = _lib.PixelSetColor
PixelSetColor.restype = MagickBooleanType
PixelSetColor.argtypes = [POINTER(PixelWand), STRING]
ClonePixelWand = _lib.ClonePixelWand
ClonePixelWand.restype = POINTER(PixelWand)
ClonePixelWand.argtypes = [POINTER(PixelWand)]
ClonePixelWands = _lib.ClonePixelWands
ClonePixelWands.restype = POINTER(POINTER(PixelWand))
ClonePixelWands.argtypes = [POINTER(POINTER(PixelWand)), size_t]
DestroyPixelWand = _lib.DestroyPixelWand
DestroyPixelWand.restype = POINTER(PixelWand)
DestroyPixelWand.argtypes = [POINTER(PixelWand)]
DestroyPixelWands = _lib.DestroyPixelWands
DestroyPixelWands.restype = POINTER(POINTER(PixelWand))
DestroyPixelWands.argtypes = [POINTER(POINTER(PixelWand)), size_t]
NewPixelWand = _lib.NewPixelWand
NewPixelWand.restype = POINTER(PixelWand)
NewPixelWand.argtypes = []
NewPixelWands = _lib.NewPixelWands
NewPixelWands.restype = POINTER(POINTER(PixelWand))
NewPixelWands.argtypes = [size_t]
PixelGetAlphaQuantum = _lib.PixelGetAlphaQuantum
PixelGetAlphaQuantum.restype = Quantum
PixelGetAlphaQuantum.argtypes = [POINTER(PixelWand)]
PixelGetBlackQuantum = _lib.PixelGetBlackQuantum
PixelGetBlackQuantum.restype = Quantum
PixelGetBlackQuantum.argtypes = [POINTER(PixelWand)]
PixelGetBlueQuantum = _lib.PixelGetBlueQuantum
PixelGetBlueQuantum.restype = Quantum
PixelGetBlueQuantum.argtypes = [POINTER(PixelWand)]
PixelGetCyanQuantum = _lib.PixelGetCyanQuantum
PixelGetCyanQuantum.restype = Quantum
PixelGetCyanQuantum.argtypes = [POINTER(PixelWand)]
PixelGetGreenQuantum = _lib.PixelGetGreenQuantum
PixelGetGreenQuantum.restype = Quantum
PixelGetGreenQuantum.argtypes = [POINTER(PixelWand)]
PixelGetMagentaQuantum = _lib.PixelGetMagentaQuantum
PixelGetMagentaQuantum.restype = Quantum
PixelGetMagentaQuantum.argtypes = [POINTER(PixelWand)]
PixelGetOpacityQuantum = _lib.PixelGetOpacityQuantum
PixelGetOpacityQuantum.restype = Quantum
PixelGetOpacityQuantum.argtypes = [POINTER(PixelWand)]
PixelGetRedQuantum = _lib.PixelGetRedQuantum
PixelGetRedQuantum.restype = Quantum
PixelGetRedQuantum.argtypes = [POINTER(PixelWand)]
PixelGetYellowQuantum = _lib.PixelGetYellowQuantum
PixelGetYellowQuantum.restype = Quantum
PixelGetYellowQuantum.argtypes = [POINTER(PixelWand)]
PixelGetColorCount = _lib.PixelGetColorCount
PixelGetColorCount.restype = size_t
PixelGetColorCount.argtypes = [POINTER(PixelWand)]
ClearPixelWand = _lib.ClearPixelWand
ClearPixelWand.restype = None
ClearPixelWand.argtypes = [POINTER(PixelWand)]
PixelGetHSL = _lib.PixelGetHSL
PixelGetHSL.restype = None
PixelGetHSL.argtypes = [POINTER(PixelWand), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
PixelGetQuantumColor = _lib.PixelGetQuantumColor
PixelGetQuantumColor.restype = None
PixelGetQuantumColor.argtypes = [POINTER(PixelWand), POINTER(PixelPacket)]
PixelSetAlpha = _lib.PixelSetAlpha
PixelSetAlpha.restype = None
PixelSetAlpha.argtypes = [POINTER(PixelWand), c_double]
PixelSetAlphaQuantum = _lib.PixelSetAlphaQuantum
PixelSetAlphaQuantum.restype = None
PixelSetAlphaQuantum.argtypes = [POINTER(PixelWand), Quantum]
PixelSetBlack = _lib.PixelSetBlack
PixelSetBlack.restype = None
PixelSetBlack.argtypes = [POINTER(PixelWand), c_double]
PixelSetBlackQuantum = _lib.PixelSetBlackQuantum
PixelSetBlackQuantum.restype = None
PixelSetBlackQuantum.argtypes = [POINTER(PixelWand), Quantum]
PixelSetBlue = _lib.PixelSetBlue
PixelSetBlue.restype = None
PixelSetBlue.argtypes = [POINTER(PixelWand), c_double]
PixelSetBlueQuantum = _lib.PixelSetBlueQuantum
PixelSetBlueQuantum.restype = None
PixelSetBlueQuantum.argtypes = [POINTER(PixelWand), Quantum]
PixelSetColorFromWand = _lib.PixelSetColorFromWand
PixelSetColorFromWand.restype = None
PixelSetColorFromWand.argtypes = [POINTER(PixelWand), POINTER(PixelWand)]
PixelSetColorCount = _lib.PixelSetColorCount
PixelSetColorCount.restype = None
PixelSetColorCount.argtypes = [POINTER(PixelWand), size_t]
PixelSetCyan = _lib.PixelSetCyan
PixelSetCyan.restype = None
PixelSetCyan.argtypes = [POINTER(PixelWand), c_double]
PixelSetCyanQuantum = _lib.PixelSetCyanQuantum
PixelSetCyanQuantum.restype = None
PixelSetCyanQuantum.argtypes = [POINTER(PixelWand), Quantum]
PixelSetFuzz = _lib.PixelSetFuzz
PixelSetFuzz.restype = None
PixelSetFuzz.argtypes = [POINTER(PixelWand), c_double]
PixelSetGreen = _lib.PixelSetGreen
PixelSetGreen.restype = None
PixelSetGreen.argtypes = [POINTER(PixelWand), c_double]
PixelSetGreenQuantum = _lib.PixelSetGreenQuantum
PixelSetGreenQuantum.restype = None
PixelSetGreenQuantum.argtypes = [POINTER(PixelWand), Quantum]
PixelSetHSL = _lib.PixelSetHSL
PixelSetHSL.restype = None
PixelSetHSL.argtypes = [POINTER(PixelWand), c_double, c_double, c_double]
PixelSetIndex = _lib.PixelSetIndex
PixelSetIndex.restype = None
PixelSetIndex.argtypes = [POINTER(PixelWand), IndexPacket]
PixelSetMagenta = _lib.PixelSetMagenta
PixelSetMagenta.restype = None
PixelSetMagenta.argtypes = [POINTER(PixelWand), c_double]
PixelSetMagentaQuantum = _lib.PixelSetMagentaQuantum
PixelSetMagentaQuantum.restype = None
PixelSetMagentaQuantum.argtypes = [POINTER(PixelWand), Quantum]
PixelSetMagickColor = _lib.PixelSetMagickColor
PixelSetMagickColor.restype = None
PixelSetMagickColor.argtypes = [POINTER(PixelWand), POINTER(MagickPixelPacket)]
PixelSetOpacity = _lib.PixelSetOpacity
PixelSetOpacity.restype = None
PixelSetOpacity.argtypes = [POINTER(PixelWand), c_double]
PixelSetOpacityQuantum = _lib.PixelSetOpacityQuantum
PixelSetOpacityQuantum.restype = None
PixelSetOpacityQuantum.argtypes = [POINTER(PixelWand), Quantum]
PixelSetQuantumColor = _lib.PixelSetQuantumColor
PixelSetQuantumColor.restype = None
PixelSetQuantumColor.argtypes = [POINTER(PixelWand), POINTER(PixelPacket)]
PixelSetRed = _lib.PixelSetRed
PixelSetRed.restype = None
PixelSetRed.argtypes = [POINTER(PixelWand), c_double]
PixelSetRedQuantum = _lib.PixelSetRedQuantum
PixelSetRedQuantum.restype = None
PixelSetRedQuantum.argtypes = [POINTER(PixelWand), Quantum]
PixelSetYellow = _lib.PixelSetYellow
PixelSetYellow.restype = None
PixelSetYellow.argtypes = [POINTER(PixelWand), c_double]
PixelSetYellowQuantum = _lib.PixelSetYellowQuantum
PixelSetYellowQuantum.restype = None
PixelSetYellowQuantum.argtypes = [POINTER(PixelWand), Quantum]
StreamImageCommand = _lib.StreamImageCommand
StreamImageCommand.restype = MagickBooleanType
StreamImageCommand.argtypes = [POINTER(ImageInfo), c_int, POINTER(STRING), POINTER(STRING), POINTER(ExceptionInfo)]
class _IO_marker(Structure):
    pass
__off_t = c_long
_IO_lock_t = None
__off64_t = c_long
_IO_FILE._fields_ = [
    ('_flags', c_int),
    ('_IO_read_ptr', STRING),
    ('_IO_read_end', STRING),
    ('_IO_read_base', STRING),
    ('_IO_write_base', STRING),
    ('_IO_write_ptr', STRING),
    ('_IO_write_end', STRING),
    ('_IO_buf_base', STRING),
    ('_IO_buf_end', STRING),
    ('_IO_save_base', STRING),
    ('_IO_backup_base', STRING),
    ('_IO_save_end', STRING),
    ('_markers', POINTER(_IO_marker)),
    ('_chain', POINTER(_IO_FILE)),
    ('_fileno', c_int),
    ('_flags2', c_int),
    ('_old_offset', __off_t),
    ('_cur_column', c_ushort),
    ('_vtable_offset', c_byte),
    ('_shortbuf', c_char * 1),
    ('_lock', POINTER(_IO_lock_t)),
    ('_offset', __off64_t),
    ('__pad1', c_void_p),
    ('__pad2', c_void_p),
    ('__pad3', c_void_p),
    ('__pad4', c_void_p),
    ('__pad5', size_t),
    ('_mode', c_int),
    ('_unused2', c_char * 20),
]
_CacheView._fields_ = [
]
_CoderInfo._fields_ = [
    ('path', STRING),
    ('magick', STRING),
    ('name', STRING),
    ('exempt', MagickBooleanType),
    ('stealth', MagickBooleanType),
    ('previous', POINTER(_CoderInfo)),
    ('next', POINTER(_CoderInfo)),
    ('signature', size_t),
]
_MagickPixelPacket._fields_ = [
    ('storage_class', ClassType),
    ('colorspace', ColorspaceType),
    ('matte', MagickBooleanType),
    ('fuzz', c_double),
    ('depth', size_t),
    ('red', MagickRealType),
    ('green', MagickRealType),
    ('blue', MagickRealType),
    ('opacity', MagickRealType),
    ('index', MagickRealType),
]
_ColorInfo._fields_ = [
    ('path', STRING),
    ('name', STRING),
    ('compliance', ComplianceType),
    ('color', MagickPixelPacket),
    ('exempt', MagickBooleanType),
    ('stealth', MagickBooleanType),
    ('previous', POINTER(_ColorInfo)),
    ('next', POINTER(_ColorInfo)),
    ('signature', size_t),
]
_ErrorInfo._fields_ = [
    ('mean_error_per_pixel', c_double),
    ('normalized_mean_error', c_double),
    ('normalized_maximum_error', c_double),
]
_Ascii85Info._fields_ = [
]
_ConfigureInfo._fields_ = [
    ('path', STRING),
    ('name', STRING),
    ('value', STRING),
    ('exempt', MagickBooleanType),
    ('stealth', MagickBooleanType),
    ('previous', POINTER(_ConfigureInfo)),
    ('next', POINTER(_ConfigureInfo)),
    ('signature', size_t),
]
_FrameInfo._fields_ = [
    ('width', size_t),
    ('height', size_t),
    ('x', ssize_t),
    ('y', ssize_t),
    ('inner_bevel', ssize_t),
    ('outer_bevel', ssize_t),
]
_DelegateInfo._fields_ = [
    ('path', STRING),
    ('decode', STRING),
    ('encode', STRING),
    ('commands', STRING),
    ('mode', ssize_t),
    ('thread_support', MagickBooleanType),
    ('spawn', MagickBooleanType),
    ('stealth', MagickBooleanType),
    ('previous', POINTER(_DelegateInfo)),
    ('next', POINTER(_DelegateInfo)),
    ('signature', size_t),
]
_ViewInfo._fields_ = [
]
_ImageAttribute._fields_ = [
    ('key', STRING),
    ('value', STRING),
    ('compression', MagickBooleanType),
    ('previous', POINTER(_ImageAttribute)),
    ('next', POINTER(_ImageAttribute)),
]
_PointInfo._fields_ = [
    ('x', c_double),
    ('y', c_double),
]
_StopInfo._fields_ = [
    ('color', MagickPixelPacket),
    ('offset', MagickRealType),
]
_RectangleInfo._fields_ = [
    ('width', size_t),
    ('height', size_t),
    ('x', ssize_t),
    ('y', ssize_t),
]
_SegmentInfo._fields_ = [
    ('x1', c_double),
    ('y1', c_double),
    ('x2', c_double),
    ('y2', c_double),
]
_GradientInfo._fields_ = [
    ('type', GradientType),
    ('bounding_box', RectangleInfo),
    ('gradient_vector', SegmentInfo),
    ('stops', POINTER(StopInfo)),
    ('number_stops', size_t),
    ('spread', SpreadMethod),
    ('debug', MagickBooleanType),
    ('signature', size_t),
    ('center', PointInfo),
    ('radius', MagickRealType),
]
_ElementReference._fields_ = [
    ('id', STRING),
    ('type', ReferenceType),
    ('gradient', GradientInfo),
    ('signature', size_t),
    ('previous', POINTER(_ElementReference)),
    ('next', POINTER(_ElementReference)),
]
_AffineMatrix._fields_ = [
    ('sx', c_double),
    ('rx', c_double),
    ('ry', c_double),
    ('sy', c_double),
    ('tx', c_double),
    ('ty', c_double),
]
_PixelPacket._fields_ = [
    ('blue', Quantum),
    ('green', Quantum),
    ('red', Quantum),
    ('opacity', Quantum),
]
_DrawInfo._fields_ = [
    ('primitive', STRING),
    ('geometry', STRING),
    ('viewbox', RectangleInfo),
    ('affine', AffineMatrix),
    ('gravity', GravityType),
    ('fill', PixelPacket),
    ('stroke', PixelPacket),
    ('stroke_width', c_double),
    ('gradient', GradientInfo),
    ('fill_pattern', POINTER(Image)),
    ('tile', POINTER(Image)),
    ('stroke_pattern', POINTER(Image)),
    ('stroke_antialias', MagickBooleanType),
    ('text_antialias', MagickBooleanType),
    ('fill_rule', FillRule),
    ('linecap', LineCap),
    ('linejoin', LineJoin),
    ('miterlimit', size_t),
    ('dash_offset', c_double),
    ('decorate', DecorationType),
    ('compose', CompositeOperator),
    ('text', STRING),
    ('face', size_t),
    ('font', STRING),
    ('metrics', STRING),
    ('family', STRING),
    ('style', StyleType),
    ('stretch', StretchType),
    ('weight', size_t),
    ('encoding', STRING),
    ('pointsize', c_double),
    ('density', STRING),
    ('align', AlignType),
    ('undercolor', PixelPacket),
    ('border_color', PixelPacket),
    ('server_name', STRING),
    ('dash_pattern', POINTER(c_double)),
    ('clip_mask', STRING),
    ('bounds', SegmentInfo),
    ('clip_units', ClipPathUnits),
    ('opacity', Quantum),
    ('render', MagickBooleanType),
    ('element_reference', ElementReference),
    ('debug', MagickBooleanType),
    ('signature', size_t),
    ('kerning', c_double),
    ('interword_spacing', c_double),
    ('interline_spacing', c_double),
    ('direction', DirectionType),
]
_PrimitiveInfo._fields_ = [
    ('point', PointInfo),
    ('coordinates', size_t),
    ('primitive', PrimitiveType),
    ('method', PaintMethod),
    ('text', STRING),
]
_TypeMetric._fields_ = [
    ('pixels_per_em', PointInfo),
    ('ascent', c_double),
    ('descent', c_double),
    ('width', c_double),
    ('height', c_double),
    ('max_advance', c_double),
    ('underline_position', c_double),
    ('underline_thickness', c_double),
    ('bounds', SegmentInfo),
    ('origin', PointInfo),
]
_ExceptionInfo._fields_ = [
    ('severity', ExceptionType),
    ('error_number', c_int),
    ('reason', STRING),
    ('description', STRING),
    ('exceptions', c_void_p),
    ('relinquish', MagickBooleanType),
    ('semaphore', POINTER(SemaphoreInfo)),
    ('signature', size_t),
]
_ChannelFeatures._fields_ = [
    ('angular_second_moment', c_double * 4),
    ('contrast', c_double * 4),
    ('correlation', c_double * 4),
    ('variance_sum_of_squares', c_double * 4),
    ('inverse_difference_moment', c_double * 4),
    ('sum_average', c_double * 4),
    ('sum_variance', c_double * 4),
    ('sum_entropy', c_double * 4),
    ('entropy', c_double * 4),
    ('difference_variance', c_double * 4),
    ('difference_entropy', c_double * 4),
    ('measure_of_correlation_1', c_double * 4),
    ('measure_of_correlation_2', c_double * 4),
    ('maximum_correlation_coefficient', c_double * 4),
]
_GeometryInfo._fields_ = [
    ('rho', c_double),
    ('sigma', c_double),
    ('xi', c_double),
    ('psi', c_double),
    ('chi', c_double),
]
_OffsetInfo._fields_ = [
    ('x', ssize_t),
    ('y', ssize_t),
]
_HashmapInfo._fields_ = [
]
_LinkedListInfo._fields_ = [
]
_ColorPacket._fields_ = [
    ('pixel', PixelPacket),
    ('index', IndexPacket),
    ('count', MagickSizeType),
]
_PrimaryInfo._fields_ = [
    ('x', c_double),
    ('y', c_double),
    ('z', c_double),
]
_ChromaticityInfo._fields_ = [
    ('red_primary', PrimaryInfo),
    ('green_primary', PrimaryInfo),
    ('blue_primary', PrimaryInfo),
    ('white_point', PrimaryInfo),
]
_Timer._fields_ = [
    ('start', c_double),
    ('stop', c_double),
    ('total', c_double),
]
_TimerInfo._fields_ = [
    ('user', Timer),
    ('elapsed', Timer),
    ('state', TimerState),
    ('signature', size_t),
]
_ProfileInfo._fields_ = [
    ('name', STRING),
    ('length', size_t),
    ('info', POINTER(c_ubyte)),
    ('signature', size_t),
]
_Image._fields_ = [
    ('storage_class', ClassType),
    ('colorspace', ColorspaceType),
    ('compression', CompressionType),
    ('quality', size_t),
    ('orientation', OrientationType),
    ('taint', MagickBooleanType),
    ('matte', MagickBooleanType),
    ('columns', size_t),
    ('rows', size_t),
    ('depth', size_t),
    ('colors', size_t),
    ('colormap', POINTER(PixelPacket)),
    ('background_color', PixelPacket),
    ('border_color', PixelPacket),
    ('matte_color', PixelPacket),
    ('gamma', c_double),
    ('chromaticity', ChromaticityInfo),
    ('rendering_intent', RenderingIntent),
    ('profiles', c_void_p),
    ('units', ResolutionType),
    ('montage', STRING),
    ('directory', STRING),
    ('geometry', STRING),
    ('offset', ssize_t),
    ('x_resolution', c_double),
    ('y_resolution', c_double),
    ('page', RectangleInfo),
    ('extract_info', RectangleInfo),
    ('tile_info', RectangleInfo),
    ('bias', c_double),
    ('blur', c_double),
    ('fuzz', c_double),
    ('filter', FilterTypes),
    ('interlace', InterlaceType),
    ('endian', EndianType),
    ('gravity', GravityType),
    ('compose', CompositeOperator),
    ('dispose', DisposeType),
    ('clip_mask', POINTER(_Image)),
    ('scene', size_t),
    ('delay', size_t),
    ('ticks_per_second', ssize_t),
    ('iterations', size_t),
    ('total_colors', size_t),
    ('start_loop', ssize_t),
    ('error', ErrorInfo),
    ('timer', TimerInfo),
    ('progress_monitor', MagickProgressMonitor),
    ('client_data', c_void_p),
    ('cache', c_void_p),
    ('attributes', c_void_p),
    ('ascii85', POINTER(Ascii85Info)),
    ('blob', POINTER(BlobInfo)),
    ('filename', c_char * 4096),
    ('magick_filename', c_char * 4096),
    ('magick', c_char * 4096),
    ('magick_columns', size_t),
    ('magick_rows', size_t),
    ('exception', ExceptionInfo),
    ('debug', MagickBooleanType),
    ('reference_count', ssize_t),
    ('semaphore', POINTER(SemaphoreInfo)),
    ('color_profile', ProfileInfo),
    ('iptc_profile', ProfileInfo),
    ('generic_profile', POINTER(ProfileInfo)),
    ('generic_profiles', size_t),
    ('signature', size_t),
    ('previous', POINTER(_Image)),
    ('list', POINTER(_Image)),
    ('next', POINTER(_Image)),
    ('interpolate', InterpolatePixelMethod),
    ('black_point_compensation', MagickBooleanType),
    ('transparent_color', PixelPacket),
    ('mask', POINTER(_Image)),
    ('tile_offset', RectangleInfo),
    ('properties', c_void_p),
    ('artifacts', c_void_p),
    ('type', ImageType),
    ('dither', MagickBooleanType),
    ('extent', MagickSizeType),
    ('ping', MagickBooleanType),
]
_ImageInfo._fields_ = [
    ('compression', CompressionType),
    ('orientation', OrientationType),
    ('temporary', MagickBooleanType),
    ('adjoin', MagickBooleanType),
    ('affirm', MagickBooleanType),
    ('antialias', MagickBooleanType),
    ('size', STRING),
    ('extract', STRING),
    ('page', STRING),
    ('scenes', STRING),
    ('scene', size_t),
    ('number_scenes', size_t),
    ('depth', size_t),
    ('interlace', InterlaceType),
    ('endian', EndianType),
    ('units', ResolutionType),
    ('quality', size_t),
    ('sampling_factor', STRING),
    ('server_name', STRING),
    ('font', STRING),
    ('texture', STRING),
    ('density', STRING),
    ('pointsize', c_double),
    ('fuzz', c_double),
    ('background_color', PixelPacket),
    ('border_color', PixelPacket),
    ('matte_color', PixelPacket),
    ('dither', MagickBooleanType),
    ('monochrome', MagickBooleanType),
    ('colors', size_t),
    ('colorspace', ColorspaceType),
    ('type', ImageType),
    ('preview_type', PreviewType),
    ('group', ssize_t),
    ('ping', MagickBooleanType),
    ('verbose', MagickBooleanType),
    ('view', STRING),
    ('authenticate', STRING),
    ('channel', ChannelType),
    ('attributes', POINTER(Image)),
    ('options', c_void_p),
    ('progress_monitor', MagickProgressMonitor),
    ('client_data', c_void_p),
    ('cache', c_void_p),
    ('stream', StreamHandler),
    ('file', POINTER(FILE)),
    ('blob', c_void_p),
    ('length', size_t),
    ('magick', c_char * 4096),
    ('unique', c_char * 4096),
    ('zero', c_char * 4096),
    ('filename', c_char * 4096),
    ('debug', MagickBooleanType),
    ('tile', STRING),
    ('subimage', size_t),
    ('subrange', size_t),
    ('pen', PixelPacket),
    ('signature', size_t),
    ('virtual_pixel_method', VirtualPixelMethod),
    ('transparent_color', PixelPacket),
    ('profile', c_void_p),
    ('synchronize', MagickBooleanType),
]
_LocaleInfo._fields_ = [
    ('path', STRING),
    ('tag', STRING),
    ('message', STRING),
    ('stealth', MagickBooleanType),
    ('previous', POINTER(_LocaleInfo)),
    ('next', POINTER(_LocaleInfo)),
    ('signature', size_t),
]
_LogInfo._fields_ = [
]
_MagicInfo._fields_ = [
    ('path', STRING),
    ('name', STRING),
    ('target', STRING),
    ('magic', POINTER(c_ubyte)),
    ('length', size_t),
    ('offset', MagickOffsetType),
    ('exempt', MagickBooleanType),
    ('stealth', MagickBooleanType),
    ('previous', POINTER(_MagicInfo)),
    ('next', POINTER(_MagicInfo)),
    ('signature', size_t),
]
_BlobInfo._fields_ = [
]
_MagickInfo._fields_ = [
    ('name', STRING),
    ('description', STRING),
    ('version', STRING),
    ('note', STRING),
    ('module', STRING),
    ('image_info', POINTER(ImageInfo)),
    ('decoder', POINTER(DecodeImageHandler)),
    ('encoder', POINTER(EncodeImageHandler)),
    ('magick', POINTER(IsImageFormatHandler)),
    ('client_data', c_void_p),
    ('adjoin', MagickBooleanType),
    ('raw', MagickBooleanType),
    ('endian_support', MagickBooleanType),
    ('blob_support', MagickBooleanType),
    ('seekable_stream', MagickBooleanType),
    ('format_type', MagickFormatType),
    ('thread_support', MagickStatusType),
    ('stealth', MagickBooleanType),
    ('previous', POINTER(_MagickInfo)),
    ('next', POINTER(_MagickInfo)),
    ('signature', size_t),
]
_MimeInfo._fields_ = [
]
_ModuleInfo._fields_ = [
    ('path', STRING),
    ('tag', STRING),
    ('handle', c_void_p),
    ('unregister_module', CFUNCTYPE(None)),
    ('register_module', CFUNCTYPE(size_t)),
    ('timestamp', time_t),
    ('stealth', MagickBooleanType),
    ('previous', POINTER(_ModuleInfo)),
    ('next', POINTER(_ModuleInfo)),
    ('signature', size_t),
]
_MontageInfo._fields_ = [
    ('geometry', STRING),
    ('tile', STRING),
    ('title', STRING),
    ('frame', STRING),
    ('texture', STRING),
    ('font', STRING),
    ('pointsize', c_double),
    ('border_width', size_t),
    ('shadow', MagickBooleanType),
    ('fill', PixelPacket),
    ('stroke', PixelPacket),
    ('background_color', PixelPacket),
    ('border_color', PixelPacket),
    ('matte_color', PixelPacket),
    ('gravity', GravityType),
    ('filename', c_char * 4096),
    ('debug', MagickBooleanType),
    ('signature', size_t),
]
_OptionInfo._fields_ = [
    ('mnemonic', STRING),
    ('type', ssize_t),
    ('stealth', MagickBooleanType),
]
_DoublePixelPacket._fields_ = [
    ('red', c_double),
    ('green', c_double),
    ('blue', c_double),
    ('opacity', c_double),
    ('index', c_double),
]
_LongPixelPacket._fields_ = [
    ('red', c_uint),
    ('green', c_uint),
    ('blue', c_uint),
    ('opacity', c_uint),
    ('index', c_uint),
]
_PolicyInfo._fields_ = [
]
_QuantizeInfo._fields_ = [
    ('number_colors', size_t),
    ('tree_depth', size_t),
    ('dither', MagickBooleanType),
    ('colorspace', ColorspaceType),
    ('measure_error', MagickBooleanType),
    ('signature', size_t),
    ('dither_method', DitherMethod),
]
_QuantumInfo._fields_ = [
]
_RandomInfo._fields_ = [
]
_ResampleFilter._fields_ = [
]
_SplayTreeInfo._fields_ = [
]
_ChannelStatistics._fields_ = [
    ('depth', size_t),
    ('minima', c_double),
    ('maxima', c_double),
    ('mean', c_double),
    ('standard_deviation', c_double),
    ('kurtosis', c_double),
    ('skewness', c_double),
]
_StringInfo._fields_ = [
    ('path', c_char * 4096),
    ('datum', POINTER(c_ubyte)),
    ('length', size_t),
    ('signature', size_t),
]
_ThresholdMap._fields_ = [
]
_TokenInfo._fields_ = [
]
_TypeInfo._fields_ = [
    ('face', size_t),
    ('path', STRING),
    ('name', STRING),
    ('description', STRING),
    ('family', STRING),
    ('style', StyleType),
    ('stretch', StretchType),
    ('weight', size_t),
    ('encoding', STRING),
    ('foundry', STRING),
    ('format', STRING),
    ('metrics', STRING),
    ('glyphs', STRING),
    ('stealth', MagickBooleanType),
    ('previous', POINTER(_TypeInfo)),
    ('next', POINTER(_TypeInfo)),
    ('signature', size_t),
]
_XMLTreeInfo._fields_ = [
]
_XImportInfo._fields_ = [
    ('frame', MagickBooleanType),
    ('borders', MagickBooleanType),
    ('screen', MagickBooleanType),
    ('descend', MagickBooleanType),
    ('silent', MagickBooleanType),
]
_MagickWand._fields_ = [
]
_DrawingWand._fields_ = [
]
_PixelIterator._fields_ = [
]
_PixelView._fields_ = [
]
_PixelWand._fields_ = [
]
__va_list_tag._fields_ = [
]
_IO_marker._fields_ = [
    ('_next', POINTER(_IO_marker)),
    ('_sbuf', POINTER(_IO_FILE)),
    ('_pos', c_int),
]
__all__ = ['RGBOQuantum', 'OpaqueImage', 'ManhattanKernel',
           'LocaleLower', 'GrayVirtualPixelMethod',
           'PaletteMatteType', 'SolarizeImage', 'MagickSteganoImage',
           'MagickSetBackgroundColor', 'SetLogName',
           'MinusCompositeOp', '_ErrorInfo', 'GetMimeInfo',
           'MorphologyMethod', 'ChopImage', 'MagickClipPathImage',
           'ParseImageGeometry', 'SyncNextImageInList',
           'MagickGetAntialias', 'DecorationType', 'LineEndsKernel',
           'MagickPolicyOptions', 'FatalErrorHandler',
           'GetOneCacheViewVirtualMethodPixel', 'ResetMagickMemory',
           'OutCompositeOp', 'GetOneCacheViewAuthenticPixel',
           'LocaleComponentTerminus', 'DelegatePolicyDomain',
           'IsMagickTrue', 'MagickRealType', 'NewPixelViewRegion',
           'StereoAnaglyphImage', 'GaussianNoiseEvaluateOperator',
           'DisposeType', 'HorizontalTileEdgeVirtualPixelMethod',
           'IsRightsAuthorized', '_OptionInfo', 'PixelGetCyan',
           'DrawPoint', 'BackgroundVirtualPixelMethod',
           'MagickImageListOptions', '__va_list_tag', '__off64_t',
           'AllocateSemaphoreInfo', 'ForgetGravity', 'StopInfo',
           'RelinquishMagickMatrix', 'UndefinedPathUnits',
           'DistanceMorphology', 'MagickWriteImagesFile',
           'UndefinedPreview', 'GetMagickPrecision', '_PrimitiveInfo',
           'PaintMethod', 'ExceptionType',
           'MagickSetImageBackgroundColor', 'MagickGetImageRegion',
           'AcquireMagickMatrix', 'ClearPixelWand', 'BlackChannel',
           'CacheEvent', 'AcquireImageColormap',
           'PixelSetBlackQuantum', 'GetImageFromMagickWand',
           'LineJoin', 'LiberateSemaphoreInfo',
           'OrderedPosterizeImage', '_DoublePixelPacket',
           '_MontageInfo', 'DrawSetClipRule', 'LeftBottomOrientation',
           'MagickSetImageOpacity', 'MagickGetIteratorIndex',
           'GetMagickPageSize', 'StreamFatalError',
           'AcquireExceptionInfo', 'StringToStringInfo', 'ShortPixel',
           'MagickSetPassphrase', 'MagickGetNumberImages',
           'IsMagickWand', '_Image', 'CorruptImageFatalError',
           'CoderWarning', 'MagickThumbnailImage', 'TriangleFilter',
           'CopyMagickString', 'AcquireIndexes',
           'DestroyImageProperties', 'GetMagickList',
           'GetDelegateCommand', 'SignedQuantumFormat',
           'MagickSetImagePage', 'DestroyMagickRegistry',
           'DrawGetStrokeLineCap', 'HashPointerType',
           'PutEntryInHashmap', 'MagickOptionToMnemonic',
           'GetMagickCopyright', 'SaturationIntent',
           'MagickDecorateOptions', 'ConcatenateString',
           'AcquireCacheViewPixels', 'OptionWarning',
           'PrependImageToList', '_RectangleInfo', 'SetImageClipMask',
           '_IO_FILE', 'RotatePreview', 'DestroyMagickMemory',
           'MagickGetImageSignature', 'GeometryInfo',
           'ExtractSubimageFromImage', 'UpdatePixelViewIterator',
           'GetImageChannelFeatures', 'AreaValue',
           'MagickResizeImage', 'DrawGetStrokeLineJoin',
           'ChannelStatistics', 'DrawPathMoveToAbsolute',
           'StripString', 'GRAYColorspace', 'ResizeQuantumMemory',
           'GrayscaleMatteType', 'MagickGetImageChannelDistortion',
           'SetXMLTreeContent', 'ArcPrimitive', 'CubicFilter',
           'ResetImageProfileIterator', '_MagicInfo',
           'AcquireOneCacheViewPixel', 'SetLogEventMask',
           'SetPixelViewIterator', 'QueryMagickColor',
           'MagickDeleteImageProperty', 'BrightnessContrastImage',
           'GetImageGeometry', 'MagickCoreTerminus', 'ViewInfo',
           'GetOnePixel', 'UnregisterStaticModules',
           'RandomChannelThresholdImage', 'RandomNoise',
           'MattePrimitive', 'GetNextImageProfile', 'ClearLinkedList',
           'MagickPaintOpaqueImageChannel',
           'ThresholdBlackEvaluateOperator', 'MogrifyImages',
           'MagickGammaImage', 'GetLocaleList',
           'MagickDelegateOptions', 'GetOneCacheViewVirtualPixel',
           'SetMagickMemoryMethods', 'ThreadResource',
           'RemoveImageProperty', 'MagickSigmoidalContrastImage',
           'RandomError', 'RootPath', 'DeskewImage',
           'MagickDeskewImage', 'OpenMorphology', 'PixelSetHSL',
           'SyncCacheViewAuthenticPixels', 'ModulusAddCompositeOp',
           'GeometryFlags', 'SetImageBackgroundColor',
           'PixelSetOpacity', 'DefineImageArtifact',
           'PixelGetGreenQuantum', 'StringToArgv',
           'MagickDisposeOptions', 'AppendImageFormat',
           'SetImageRegistry', 'DrawGetOpacity',
           'RightTopOrientation', 'BorderImage', 'ConstituteImage',
           'GetLogInfoList', 'GrayChannels', 'DrawPathLineToAbsolute',
           'MosaicLayer', 'NormalizeImage', 'QuantizeImages',
           'TransverseImage', 'MitchellFilter', 'MagickSetColorspace',
           'GaussianFilter', 'ParseGravityGeometry',
           'SortColormapByIntensity', 'TransferPixelViewMethod',
           'MissingDelegateWarning', 'GetTypeInfoByFamily',
           'GradientReference', 'PixelGetBlackQuantum', 'MorphImages',
           'DrawGetExceptionType', '_LocaleInfo', 'FilterImage',
           'ResetImageRegistryIterator', 'UndefinedMetric',
           'MagickMosaicImages', 'AnnotateEvent',
           'GetImageListLength', 'X11Compliance',
           'MagickSetImageUnits', 'CloneMontageInfo',
           'FreiChenKernel', 'DestroyKernelInfo',
           'MagickHaldClutImageChannel', 'MagickGetImageBorderColor',
           'PixelSetMagenta', 'MagickColorMatrixImage',
           'MagickStyleOptions', 'FloydSteinbergDitherMethod',
           'MagickGetImageType', 'SplineInterpolatePixel',
           'MagickOptimizeImageLayers', 'TransmitType', 'StartTimer',
           'SouthGravity', 'UndefinedDitherMethod', 'NormalStretch',
           'InsertTagIntoXMLTree', 'GetImageException',
           'ResourceComponentGenesis', 'SkeletonKernel', 'DrawInfo',
           'QuantumAlphaType', 'TransformHSL', '_ColorInfo',
           'ImplodePreview', 'MagickNextImage', 'Tokenizer',
           'StorageType', 'LevelColorsImageChannel', 'GaussianKernel',
           'N14pthread_cond_t4DOT_17E', 'AppendValueToLinkedList',
           'MagickThreadSupport', 'ExportQuantumPixels',
           'SegmentInfo', '_ImageInfo', 'UndefinedInterlace',
           'GetNextImageProperty', 'RGBChannels',
           'TransparentPaintImage', 'ImageToFile',
           'MagickVirtualPixelOptions', 'RingKernel',
           'AccelerateConvolveImage', 'MagickGetImageIndex',
           'MagickExportImagePixels', 'MagickEvaluateOperator',
           'MagickClassOptions', 'PizCompression', 'ColorizeImage',
           'PixelGetYellow', 'IsPathAccessible',
           'MeshInterpolatePixel', 'LabColorspace',
           'MagickGetOptions', 'DrawGetClipRule', 'UndefinedRule',
           'DrawPathCurveToSmoothRelative',
           'MagickAdaptiveSharpenImageChannel', 'DrawGetFontFamily',
           'ParseAffineGeometry', 'Rec709YCbCrColorspace',
           'DrawGetTextAlignment', 'MagickGetImageGamma',
           'AreaResource', 'CirclePrimitive',
           'SemaphoreComponentTerminus', 'LocaleEvent',
           'MagickSetImageChannelDepth', 'PixelSetMagentaQuantum',
           'CatchException', 'SigmoidalContrastImageChannel',
           'DrawGetStrokeOpacity', 'CloneDrawingWand',
           'AcquirePixelCachePixels', 'BlackQuantum',
           'sRGBColorspace', 'CloneImageProperties', 'ComplianceType',
           'MagickImportImagePixels', 'GetImageInfoFile',
           'CenterGravity', 'GetTypeInfoList', 'SetImageDepth',
           'ChannelImage', 'GetNumberOfEntriesInHashmap',
           'MagickIdentifyImage', 'MagickFlattenImages',
           'OrEvaluateOperator', 'ReadMode', 'FileToBlob',
           'ReferenceImage', 'DelegateComponentGenesis',
           'Ascii85Encode', 'ConvertValidate', 'CoalesceImages',
           'ReferenceType', 'OptimizeLayer', 'SetQuantumFormat',
           'CombineImages', 'GetImageClipMask',
           'MagickTransparentPaintImage', 'UndefinedCompliance',
           'RiemersmaDitherMethod', 'PopImageList', 'ModuleError',
           'PixelSetRed', 'ParseRegionGeometry',
           'MagicComponentTerminus', 'MagickPreviewImages',
           'DrawSetViewbox', 'PointFilter', 'BlurImage', 'MagicInfo',
           'DestroyMagickWand', 'MagickGetImagePixelColor',
           'SparseColorMethod', 'CenterAlign', 'PrimitiveType',
           'RemoveLastElementFromLinkedList', 'PixelGetYellowQuantum',
           'PixelGetColorAsNormalizedString', 'ListMagicInfo',
           'StreamImageCommand', 'MapImages', 'ImageRegistryType',
           'MagickCommandOptions', 'GetDelegateInfo', 'SegmentImage',
           'BoxFilter', 'InterpretImageProperties', 'CompassKernel',
           'DrawTranslate', 'QuantumFormatType',
           'SetStringInfoLength', 'MagickSetImageFuzz',
           'CloneImageArtifacts', 'MagickReduceNoiseImage',
           'FuzzyColorMatch', 'MagickPrimitiveOptions',
           'GetLastImageInList', 'FlattenLayer', 'BlobToImage',
           'PixelPacket', 'GetBlobStreamData', 'MagickShaveImage',
           'GetModuleInfo', 'ExpandAffine',
           'MagickGetInterlaceScheme', 'GetElapsedTime',
           'ColorizeCompositeOp', 'ThresholdWhiteEvaluateOperator',
           'XorCompositeOp', 'ConcatenateStringInfo',
           'TransparentPaintImageChroma', 'FileToImage',
           'IsPixelWand', 'GammaImage', 'GetAuthenticPixelQueue',
           'DrawSetStrokeMiterLimit', 'AcquireOneVirtualPixel',
           'CloneSplayTree', 'MagickLineJoinOptions', 'GetImageDepth',
           'DestroyExceptionInfo', 'HSBColorspace',
           'MagickSetImageBias', 'FaxCompression',
           'MagickMinifyImage', 'ProfileImage', 'TransformImages',
           'MagickSetImageMatteColor', 'PixelGetColorCount',
           'GetClientName', 'MagickUniqueImageColors',
           'DrawFatalError', 'MagickQueryMultilineFontMetrics',
           'GetLogList', 'SyncImagesSettings', '_ThresholdMap',
           'MagickInverseFourierTransformImage', 'ChannelFeatures',
           'GetCacheViewVirtualIndexQueue', 'OrientationType',
           'RandomThresholdImageChannel', 'DrawPushGraphicContext',
           'PeekDrawingWand', 'CopyBlueCompositeOp',
           'DestroyPixelWand', 'AcquireQuantizeInfo', 'OpenCacheView',
           'ClearCompositeOp', 'MagickColorFloodfillImage',
           'XNegative', 'IsImageFormatHandler', '_ModuleInfo',
           'SyncImageSettings', 'DispatchImage', 'GetPreviousImage',
           'FileResource', 'MagickDataTypeOptions',
           'RandomFatalError', 'MagickOrderedPosterizeImageChannel',
           'SetMagickResourceLimit', 'DeleteNodeFromSplayTree',
           'DestroyTokenInfo', 'XorEvaluateOperator',
           'StringInfoToString', 'MagickGetImageWhitePoint',
           'WriteImage', 'MagickMedianFilterImage',
           'UndefinedResource', 'SetResampleFilterVirtualPixelMethod',
           'GetNextImageRegistry', 'MagickGetImageProperties',
           'DrawGetStrokeAntialias', 'GetPixelCachePixels',
           'SepiaToneImage', 'RhoValue', 'MagickSetSamplingFactors',
           'MinimumImages', 'EqualizeImage', 'TypeComponentTerminus',
           'DivideEvaluateOperator', 'DrawSetStrokeAlpha',
           'SetAlphaChannel', 'MagickGetGravity', 'LanczosFilter',
           'PixelGetCyanQuantum', 'MagickPolicyRightsOptions',
           'GetXMLTreePath', 'ResourceLimitFatalError',
           'SetFatalErrorHandler', 'MagickGetImageRedPrimary',
           'UndefinedEndian', 'PixelClearIteratorException',
           'EqualizeImageChannel', 'UnderlineDecoration',
           'LeastSquaresAddTerms', 'MagickGetImageColormapColor',
           'MagickImplodeImage', 'ClipImage', 'SpliceImageIntoList',
           'DrawPathClose', 'PolynomialFunction', 'GetPolicyList',
           'SplitImageList', 'RoundJoin', 'IdentifyImage',
           'InterpolatePixelColor', 'GetImageQuantumDepth',
           'GetMagickOptions', '_IO_marker', 'GetImageDecoder',
           'MagickGetImagesBlob', 'MagickGetOption',
           'IsPixelIterator', 'MagickSetImageGreenPrimary',
           'GetOptimalKernelWidth', 'MagickSetProgressMonitor',
           'FormatImageAttributeList', 'MontageImages',
           'MagickFrameImage', '_IO_lock_t', 'DecodeImageHandler',
           'MagickCompressOptions', 'GetMagickDescription',
           'HanningFilter', 'MagickSepiaToneImage', 'PixelGetHSL',
           'GetCoderList', 'DrawPathLineToVerticalRelative',
           'DistortCompositeOp', 'AnimateImageCommand', 'ErrorInfo',
           'GetImagePixels', 'GetExceptionInfo', '_FrameInfo',
           'JPEG2000Compression', 'ConsolidateCMYKImages',
           'DrawGetStrokeDashArray', 'MagickSetCompressionQuality',
           'CatromFilter', 'SetImageAttribute',
           'DifferenceCompositeOp', 'ResetImageOptionIterator',
           'MontageImageCommand', 'WarningException',
           'CompositeLayers', 'Ascii85Info', 'SVGCompliance',
           'TemporaryFilename', 'ResizeImage', 'PushImageList',
           'MagickClearException', 'TypeWarning', 'OpenModules',
           'MonitorError', 'SetImageInfoBlob', 'StreamHandler',
           'MonitorWarning', 'IsHistogramImage', 'PolicyFatalError',
           'CacheFatalError', 'TrueColorMatteType', 'PingImage',
           'FlopImage', 'SetImageArtifact', 'EscapeString',
           'PixelGetBlueQuantum', 'MagickNewImage', '_ProfileInfo',
           'TypeComponentGenesis', 'FloatingPointQuantumFormat',
           'GetMagickInfo', 'ReverseImageList', 'AverageImages',
           'IsMonochromeImage', 'DisplaceCompositeOp',
           'GetPixelViewIterator', 'PixelGetPreviousIteratorRow',
           'MagickFunctionImage', 'FormatsInMemoryValidate',
           'MaxEvaluateOperator', 'ObjectBoundingBox',
           'PixelGetIndex', 'OptimizeType', 'CompositeImageChannel',
           'DestroyStringList', 'TextureImage', 'ThresholdMap',
           'CoderFatalError', 'NewMagickImage', 'SyncImagePixels',
           'GetCoderInfoList', 'IsBlobExempt', 'Image',
           'MagickSetImageDepth', 'ShadePreview', 'QuantizePreview',
           'AcquireImageInfo', 'NoPolicyRights',
           'MagickImageFilterModule', 'PopDrawingWand', 'ClutImage',
           'MagickEdgeImage', 'CheckerTileVirtualPixelMethod',
           'DrawPathCurveToRelative', 'RemoveEntryFromHashmap',
           'NormalStyle', 'HardLightCompositeOp', 'NegateImage',
           '_PointInfo', 'UnregisterMagickInfo',
           'MagickSetImageInterpolateMethod', 'ReflectSpread',
           'InitializeMagick', 'FileOpenFatalError',
           'UndefinedDistortion', 'YCCColorspace', 'GetLogName',
           'MagickOpaquePaintImageChannel', 'GetBlobSize',
           'MagickConvolveImageChannel',
           'TransparentVirtualPixelMethod', 'GetCacheViewPixels',
           'ListCoderInfo', 'GetDelegateMode',
           'AllocateImageColormap', 'GetColorInfo', 'GradientInfo',
           'ExtendedUnsignedIntegralType', 'MagickImageCoderModule',
           'PixelsPerInchResolution', 'ShiftImageList',
           'DePolarDistortion', 'ImageError', 'OpaquePaintImage',
           'MagickFillRuleOptions', 'AutoGammaImageChannel',
           'AffineMatrix', 'YPbPrColorspace', 'AcquireRandomInfo',
           'VerticalTileVirtualPixelMethod', 'PathType',
           'SemiCondensedStretch', 'MagickIntentOptions',
           'CyanChannel', 'ResetLinkedListIterator',
           'MagickSetImageInterlaceScheme', 'ColorComponentTerminus',
           'SetImageInfoFile', 'BottomRightOrientation',
           'NoCompliance', 'GradientType', 'IntegerInterpolatePixel',
           'MagickLabelImage', 'StreamWarning', 'DestroyImageOptions',
           'NoDecoration', 'ErodeMorphology', 'DrawGetFont',
           'LogEvaluateOperator', 'MagickFalse', 'DrawRender',
           'XiNegative', 'EncoderThreadSupport', 'ImportImagePixels',
           'PolygonPrimitive', 'MagickSparseColorImage', 'OptionInfo',
           'DarkenCompositeOp', 'GetNextImageOption',
           'MagickRadialBlurImageChannel', 'GetPolicyInfoList',
           'BlurImageChannel', 'EastGravity', 'GetCacheViewIndexes',
           'DrawSetFillRule', 'DrawPathLineToRelative',
           'InitializeModuleList', 'PolicyComponentTerminus',
           'MagickSpliceImage', 'ShepardsDistortion',
           'FormatMagickCaption', 'MontageMode', 'GetAuthenticPixels',
           'UndefinedResolution', 'RegistryFatalError',
           'DrawSetFillOpacity', 'GetIndexes', 'ClearDrawingWand',
           'MagickPolaroidImage', 'TopRightOrientation',
           'MagickGetImageIterations', 'RelinquishAlignedMemory',
           'InterpolatePixelMethod', 'CMYKColorspace', 'DrawSetFont',
           'AddEvaluateOperator', 'MagickCommandGenesis',
           'DeleteImageProfile', 'SetRandomTrueRandom',
           'PixelGetQuantumColor', 'CacheComponentTerminus',
           'SwirlImage', 'PushDrawingWand', 'ResourceType',
           'MagickGetFilename', 'QuantumInfo', 'UndefinedDecoration',
           'AllValues', 'GetStringInfoPath', 'UndefinedKernel',
           'RGBTransformImage', 'MagickCompareImageChannels',
           'MagickEmbossImage', 'MagickGetImageMatteColor',
           'MagickRemoveImage', 'MagickMorphologyOptions',
           '_QuantumInfo', '__time_t',
           'GetNumberOfElementsInLinkedList', 'MultilineCensus',
           'MagickSetImageProfile', 'GetImageChannelRange',
           'GrayQuantum', 'AddNoisePreview',
           'MagickRemoveImageProfile', 'CloneImageInfo',
           'KirschKernel', '__off_t', 'DrawGetTextDecoration',
           'MagickQuantumFormatOptions', 'FilterImageChannel',
           'DrawSetFontStretch', 'PixelSetGreenQuantum',
           'ChangeMaskCompositeOp', '_DrawInfo',
           'DisassociateImageStream', 'PegtopLightCompositeOp',
           'SigmoidalContrastImage', 'HitAndMissMorphology',
           'MagickPingImageFile', 'GetPixelViewHeight',
           'OverlayCompositeOp', 'ReacquireMemory', 'CacheWarning',
           'CompareHashmapStringInfo', '_MagickInfo',
           'DelegateComponentTerminus', 'NewHashmap',
           'MagickSetImageColormapColor', 'DeconstructImages',
           'GetMultilineTypeMetrics', 'ImagePrimitive',
           'B44ACompression', 'FilterTypes', 'ExceptionEvent',
           'MagickTransverseImage', 'DrawWarning', 'DiskResource',
           'SetClientPath', 'LevelImageColors', 'MagickSetFont',
           'BlackmanFilter', 'IsHashmapEmpty', 'ImagesToBlob',
           'MagickMotionBlurImageChannel', 'MagickCropImage',
           'FilterWarning', 'FileToStringInfo',
           'ScaleGeometryKernelInfo', 'SetWarningHandler',
           'GetNextKeyInHashmap', '_ExceptionInfo', 'AffinityImage',
           'UnrecognizedDispose', 'StereoImage', 'PixelSetYellow',
           'UserSpace', 'UndefinedTimerState', 'SetImageOpacity',
           'OptimizePlusImageLayers', 'UndefinedColorspace',
           'DrawRoundRectangle', 'MagickNoiseOptions',
           'DestroyMagick', 'MagickMagnifyImage', 'DrawPrimitive',
           'MagickTextureImage', 'OpenIntensityMorphology',
           'PixelGetBlack', 'TypeFatalError', 'SpliceImage',
           'SolarizePreview', 'LocaleUpper', 'RidgesKernel',
           'GetMagickFeatures', 'CopyCyanCompositeOp',
           'GetImageDynamicThreshold', 'GetImageExtent',
           'PasskeyDecipherImage', 'LockSemaphoreInfo', 'RollImage',
           'PoissonNoise', 'WestGravity', 'PixelGetAlphaQuantum',
           'ResampleImage', 'MagickEqualizeImageChannel',
           'BilinearReverseDistortion', '_TypeMetric',
           'ColorComponentGenesis', 'RelinquishUniqueFileResource',
           'DestroyImageProfiles', 'DrawAllocateWand',
           'CopyRedCompositeOp', 'MagickGravityOptions',
           'AcquireKernelInfo', 'IdentifyImageCommand',
           'PixelSetAlpha', 'UndefinedEvents',
           'MagickGetImageInterlaceScheme', 'PixelWand', 'FlipImage',
           'MagickNegateImage', 'AverageInterpolatePixel',
           'FormatString', 'MergeImageLayers', 'RemoveImageProfile',
           'ModuleFatalError', 'PlusKernel', 'EdgeDetectPreview',
           'SharpenImage', 'DrawPolygon', 'ShowKernelInfo',
           'GetFirstImageInList', 'IsPixelView', 'CropImage',
           'GetImageKurtosis', 'BlackThresholdImageChannel',
           'MagickGetSizeOffset', 'DecimalValue', 'GetMagicInfoList',
           'SizeBlob', 'ModuleComponentGenesis',
           'QueueAuthenticPixels', 'HuffmanEncodeImage', 'TypeInfo',
           'SharpenPreview', 'GetCacheViewAuthenticIndexQueue',
           'GetMontageInfo', 'RemoveDupsLayer', 'DestroyHashmap',
           'UniformNoiseEvaluateOperator', 'InsertImageInList',
           'InheritException', 'DrawingWand', 'MagickLevelImage',
           'MagickStretchOptions', 'SelectiveBlurImageChannel',
           'MagickModeOptions', 'MorphologyImage',
           'FunctionImageChannel', 'Rec709LumaColorspace',
           'MagickAdaptiveThresholdImage', 'HashmapInfo',
           'PolicyInfo', 'DelegateInfo', 'MagickWhiteThresholdImage',
           'DrawSetFontFamily', 'EdgeInMorphology',
           'GetMagickSeekableStream', 'FILE', 'DrawPopClipPath',
           'size_t', 'PixelGetBlue', 'BarrelDistortion',
           'DrawGetStrokeDashOffset', 'RemoveDuplicateLayers',
           'UndefinedGradient', 'SpreadImage',
           'MagickBlurImageChannel', 'NewPixelWands',
           'NearestNeighborInterpolatePixel', 'MagickSetCompression',
           'ReduceNoiseImage', 'BlueShiftImage', 'ExportImagePixels',
           'MagickBlurImage', 'CMYKOQuantum',
           'MagickSigmoidalContrastImageChannel',
           'EvaluateImageChannel', 'MagickGetImageResolution',
           'BilinearColorInterpolate', 'ContrastImage',
           'MagickSetImageOption', 'SrcOverCompositeOp',
           'GreenQuantum', 'MagickInfo', 'MagickSetImageExtent',
           'DrawGetClipPath', 'MagickSetImageDelay',
           'PoissonNoiseEvaluateOperator', 'HSLTransform',
           'MagickBorderImage', 'SignatureImage',
           'MeanErrorPerPixelMetric',
           'ScaleRotateTranslateDistortion', 'SeparateImages',
           'MagickGetBackgroundColor', 'RemoveNodeFromSplayTree',
           'GetMagickEndianSupport', 'UndefinedFilter',
           'ParseSizeGeometry', 'UndefinedCap', 'UniformNoise',
           'SaturateCompositeOp', 'DestroyImageArtifacts',
           'GetVirtualIndexQueue', 'MirrorVirtualPixelMethod',
           'MagickSetImageFormat', 'MagickScaleImage', 'LeftAlign',
           'RedChannel', 'PixelSetColorFromWand',
           'MagickSetImageTicksPerSecond', 'MagickGetImageGravity',
           'CoderEvent', 'HeightValue', 'DitherVirtualPixelMethod',
           'PixelGetIteratorRow', 'MeanSquaredErrorMetric',
           'GetNumberScenes', 'MultiplyEvaluateOperator', 'NoValue',
           'ClonePixelWands', 'InvokeDelegate', '_PixelIterator',
           'NewMagickWand', 'DrawScale', 'AcquireImagePixels',
           'FormatMagickStringList', 'XMLTreeInfo',
           'ResizeMagickMemory', 'DissolveCompositeOp',
           'SetLogFormat', 'UndefinedQuantumAlpha',
           'CorruptImageWarning', 'GetPixelViewX',
           'RightToLeftDirection', 'XPMCompliance', 'GetMimeList',
           'MagickLinearStretchImage', 'AdaptiveSharpenImage',
           'GetTimerInfo', 'CopyMagickMemory', 'UndefinedDispose',
           'MagickUnsharpMaskImage', 'IsHighDynamicRangeImage',
           'GetImageFromMagickRegistry', 'MagickSharpenImage',
           'RobertsKernel', 'DrawSetTextInterwordSpacing',
           'GetLocaleInfoList', 'OpacityQuantum', 'CloneImage',
           'GetImageHistogram', 'DrawAffineImage',
           'PixelSyncIterator', 'MagickGetImageVirtualPixelMethod',
           'MagickFontsOptions', 'SetQuantumPack', 'RepeatSpread',
           'CyanQuantum', 'BottomLeftOrientation',
           'RemoteDisplayCommand', 'CompareClearLayer',
           'MagickCycleColormapImage', 'DestroyXMLTree',
           'BZipCompression', 'SetQuantumDepth',
           'ErodeIntensityMorphology', 'DrawSetTextInterlineSpacing',
           'UndefinedMethod', 'DstOutCompositeOp',
           'FuzzyOpacityCompare', 'MagickSetOption', 'PaletteType',
           'RoundCap', 'GIFInterlace', 'SetQuantumPad',
           'SetStringInfoPath', 'MagickGetImageHistogram',
           'GetQuantumInfo', 'MagickSetImageRedPrimary',
           'VerticalTileEdgeVirtualPixelMethod', 'PeaksKernel',
           'GetXMLTreeAttribute', 'RectanglePrimitive',
           'FormatImagePropertyList', 'GetTypeList',
           'UnsharpMaskImage', 'FilterError', 'GetImageListIndex',
           'AcquireTokenInfo', 'DrawGetClipUnits',
           'MagickModuleOptions', 'ZipCompression',
           'CopyGreenCompositeOp', 'WandEvent', 'GetImageDistortion',
           'DespecklePreview', 'ModulateCompositeOp',
           'ClampImageChannel', 'PixelGetException',
           'MagickSimilarityImage', 'ColorPrimitive',
           'OpacityChannel', 'ParseMetaGeometry', 'DrawPushDefs',
           'GetMagicList', 'ParseMagickOption', '_ViewInfo',
           'CompareOverlayLayer', 'DestroyQuantizeInfo', 'BlobInfo',
           'DrawSetTextDecoration', 'DrawSetOpacity', 'GetCacheView',
           'GetNextImage', '_LogInfo', 'ModuleComponentTerminus',
           'DeleteImages', 'CloneImageAttributes', 'SouthEastGravity',
           'DrawImage', 'RandomWarning', 'TimerInfo',
           'TransformEvent', 'ListLogInfo',
           'GetImageVirtualPixelMethod', 'MagickWandTerminus',
           'MagickSpreadImage', 'GetImageBoundingBox', 'TraceEvent',
           'MagickAlignOptions', 'WandError',
           'DrawPathCurveToSmoothAbsolute', 'MetricType',
           'AcquireDrawInfo', 'MagickSetImageArtifact',
           'SetPixelViewMethod', 'Strip', 'AddChildToXMLTree',
           'PixelsPerCentimeterResolution', 'PaletteBilevelMatteType',
           'MagickPolicyDomainOptions', 'ThinningMorphology',
           'WandWarning', 'RGBColorspace', 'MagickQueryFonts',
           'MagickGetImageFormat', 'ConfigureError',
           'ConfigureFileToStringInfo', 'GetXMLTreeSibling',
           'PolylinePrimitive', 'DilateMorphology', 'DirectClass',
           'TileVirtualPixelMethod', 'RegisterMagickInfo',
           'PackbitsEncodeImage', 'ConvertImageCommand',
           'PreviewType', 'MagickAdaptiveSharpenImage',
           'SrcInCompositeOp', 'GetImageOption',
           'RadialBlurImageChannel', 'MagickShearImage',
           'MagickSetImageBluePrimary', 'GetStringInfoDatum',
           'MagickAddNoiseImageChannel', 'PasskeyEncipherImage',
           'GetMagickThreadSupport', '_HashmapInfo', 'EvaluateImage',
           'MedianFilterImage', 'PixelClearException', 'CometKernel',
           'LiberateMemory', 'GetConfigurePaths',
           'LevelizeImageChannel', 'StripImage',
           'MagickAnimateImages', 'SharpenImageChannel',
           'IsBlobTemporary', 'DrawGetVectorGraphics',
           'GetMagickPixelPacket', 'PixelGetColorAsString',
           'AdaptiveResizeImage', 'LevelImageChannel',
           'MissingDelegateFatalError',
           'DrawPathLineToVerticalAbsolute', 'MagickSetFilename',
           'LightenCompositeOp', 'CosineEvaluateOperator',
           'SubtractEvaluateOperator', 'LogComponentTerminus',
           'GetPathComponents', 'RemapImage', 'MagickFormatOptions',
           'FormatMagickSize', 'MagickDistortImage',
           'MagickGetImageGreenPrimary', 'SigmaValue',
           'MagickQueryFontMetrics', 'ModulusSubtractCompositeOp',
           'ChiNegative', 'MeanAbsoluteErrorMetric',
           'DrawGetTextKerning', 'SyncImageProfiles',
           'MagickFunctionImageChannel', 'IndexQuantum',
           'MagickGetType', 'TransformColorspace',
           'MagickMagicOptions', 'DrawSetTextEncoding',
           'AcquireMagickResource', 'RegistryError', 'XYZColorspace',
           'UndefinedInterpolatePixel', 'GetImageRegistry',
           'CoderPolicyDomain', 'MagickSetResourceLimit',
           'RegistryWarning', 'ImageListToArray', 'AllocateString',
           'MagickContrastStretchImageChannel', '_CoderInfo',
           'DrawSetFillPatternURL', 'MagickStatusType',
           'GetMagickAdjoin', 'ImageTransmitType', '_PixelView',
           '_XImportInfo', 'MagickSetImageIterations', 'SobelKernel',
           'DeleteImageProperty', 'GetPixelViewMethod',
           'MagickMetricOptions', 'BarrelInverseDistortion',
           'DstInCompositeOp', 'MagickSetImageRenderingIntent',
           'AcquireMemoryHandler', 'AddNoiseImage',
           'MagickSetImageOrientation', 'MagickSampleImage',
           'ActivateAlphaChannel', 'SetImageStorageClass',
           'AnimateImages', 'MagickComponentGenesis',
           'GetMimeInfoList', 'MagickSetFormat', '_OffsetInfo',
           'N4wait3DOT_6E', 'LogColorspace', 'RecolorImage',
           'ConvertRGBToHSB', 'PixelSetGreen',
           'ParseAbsoluteGeometry', 'ConvertRGBToHSL',
           'GetModuleInfoList', '_GradientInfo', 'FrameInfo',
           '_ChannelStatistics', 'SetGeometry', 'ConvolveMorphology',
           'SpreadPreview', 'IsDrawingWand', 'LaplacianNoise',
           'Quantum', '_PolicyInfo', 'UndefinedMagickLayerMethod',
           'AffineDistortion', 'MagickThresholdImageChannel',
           'MagickSetExtract', 'ModulateImage', 'GetColorTuple',
           'GetGeometry', 'UndefinedVirtualPixelMethod',
           'ContrastStretchImageChannel', 'VoronoiColorInterpolate',
           'AllocateNextImage', 'FatalErrorException', 'time_t',
           'PrintStringInfo', 'GetPixelViewWidth', 'GetMagickToken',
           '_CacheView', 'RoundRectanglePrimitive',
           'FilterPolicyDomain', 'DrawPopDefs',
           'N16pthread_rwlock_t4DOT_20E', 'QueryColorDatabase',
           'MagickGetResourceLimit', 'YValue',
           'GetMagickResourceLimit', 'DeleteImageAttribute',
           'ShearImage', 'BlackThresholdImage', 'MagickShadeImage',
           'DrawSetStrokeDashArray', 'AdaptiveSharpenImageChannel',
           'MagickGetImageAttribute', 'CloseMagickLog',
           'GetColorList', 'MagickOrientationOptions', 'RemapImages',
           'NorthWestGravity', 'MagickSegmentImage',
           'PaintOpaqueImage', 'AcquireKernelBuiltIn', 'AllChannels',
           'ObliqueStyle', 'MagickDistortOptions', 'AcquirePixels',
           'RandomComponentTerminus', 'BilinearDistortion',
           'SetMagickRegistry', 'ColorSeparationType',
           'MagickGetSamplingFactors', 'MagickOilPaintImage',
           'MagickGetReleaseDate', 'MagickDebugOptions',
           'FormatImageAttribute', 'ParseGeometry',
           'ImageLayerMethod', 'MagickGetImageProperty',
           'MagickSizeType', 'MagickModuleType',
           'MagickGetImageClipMask', 'ZLIBEncodeImage',
           'MagickGetImageBluePrimary', 'SplitStringInfo',
           'GammaImageChannel', 'IsLinkedListEmpty', '_TimerInfo',
           'GetExecutionPath', 'BilevelType', 'SetBlobExempt',
           'PolynomialColorInterpolate', 'MagickGetFont',
           'WhiteThresholdImage', 'UndefinedChannel', 'TokenInfo',
           'ChebyshevKernel', 'MagickAffineTransformImage',
           'UndefinedIntent', 'AppendImages', 'RandomInfo',
           'StreamValidate', 'DeleteImageRegistry', 'GradientImage',
           'GetImageChannelDepth', 'ShapeAlphaChannel',
           'GenerateDifferentialNoise', 'MagickWriteImageFile',
           'DescribeImage', 'MimeInfo', 'AdaptiveBlurImageChannel',
           '_PixelWand', 'TransparentColorspace', 'CloneQuantizeInfo',
           'MagickSetResolution', 'MagickInterlaceOptions',
           'MagickSetFirstIterator',
           'DrawPathCurveToQuadraticBezierRelative',
           'MagickMorphologyImage', 'MagickSetImage', 'ItalicStyle',
           'SetCacheThreshold', 'DestroyString', 'MagickTrue',
           'RemoveLastImageFromList', 'WhiteThresholdImageChannel',
           'CoderInfo', 'ResourceComponentTerminus',
           'MagickMorphologyImageChannel', 'MagickMinimumImages',
           'HueCompositeOp', 'GetConfigureOptions',
           'SrcAtopCompositeOp', 'CompressImageColormap',
           'ZipSCompression', 'AcquireMagickMemory',
           'MagickFontOptions', 'DrawGetTextInterlineSpacing',
           'AspectValue', 'MissingDelegateError', 'CloneImages',
           'UndefinedStretch', 'DrawSetTextAlignment',
           'MagickMergeImageLayers', 'SetCacheViewPixels',
           'ParseChannelOption', 'GaussianBlurImage', 'DrawComment',
           'AcquireString', 'MagickGetColorspace',
           'CacheComponentGenesis', 'MagickValidateOptions',
           'MagickSetImageIndex', 'QuantumType',
           'GetOneVirtualMagickPixel', 'ClampImage',
           'PixelSetIteratorRow', 'N4wait3DOT_7E', 'ConvertHWBToRGB',
           'ProfileInfo', 'JPEGPreview', 'WriteStream',
           'ResourceLimitWarning', 'CoalesceLayer',
           'MagickAddNoiseImage', 'MagickResolutionOptions',
           'QueryMagickColorname', 'ListMagickResourceInfo',
           '_XMLTreeInfo', 'PixelSetFuzz', 'UltraCondensedStretch',
           'CorrelateMorphology', 'PolicyEvent',
           'MagickGetImageArtifact', 'GetTypeMetrics',
           'AcquireOneCacheViewVirtualPixel', 'UndefinedAlphaChannel',
           'EvaluateImages', 'XiValue',
           'DrawPathCurveToQuadraticBezierAbsolute', 'TimerState',
           'ColorMatrixImage', 'SegmentPreview', 'NewXMLTree',
           'ExtendedRationalType', 'GetConfigureInfo',
           'AcquireAlignedMemory', 'ThresholdCompositeOp',
           'XImportImage', 'GetMagickMemoryMethods', 'RaiseImage',
           'GlobExpression', 'SyncImage', 'TranslateText',
           'MagickBrightnessContrastImageChannel',
           'InterpretImageAttributes', 'ClearMagickException',
           'CrossKernel', 'WaveImage', 'NewPixelWand',
           'PixelSetCyanQuantum', 'MogrifyImageList',
           'PushImagePixels', 'BasePath', 'DrawGetException',
           'IsImagesEqual', 'SetQuantumMinIsWhite',
           'GetMagickBlobSupport', 'IOMode', 'MagickOpaquePaintImage',
           'SquareKernel', 'MagickKernelOptions',
           'MagickSetImageResolution',
           'DrawPathLineToHorizontalRelative', 'LoGKernel',
           'EllipsePrimitive', 'ReadImage', 'NonZeroRule',
           'PixelIterator', 'AdaptiveBlurImage', 'VirtualPixelMethod',
           'Base64Decode', 'ReadImages', 'AllCompliance',
           'CompareAnyLayer', 'KernelInfoType',
           'GetImageClippingPathAttribute', 'AffinityImages',
           'AcquireOnePixel', 'ShadowImage', 'FileOpenWarning',
           'MagickGetImageArtifacts', 'GaussianNoise',
           'TextPrimitive', 'AcquireQuantumInfo',
           'MagickGetImageChannelStatistics',
           'LinearDodgeCompositeOp', 'MagickStripImage',
           'RunningTimerState', 'MagickGetImageHeight',
           'InsertValueInSortedLinkedList', 'DrawGetStrokeAlpha',
           'MagickLogEventOptions', 'PsiNegative',
           'GetImageAttribute', 'ImportExportValidate',
           'ArctanFunction', 'LeftToRightDirection',
           'ClutImageChannel', 'JPEGInterlace', 'MapImage',
           'GetImageMask', 'NormalizeValue', 'MotionBlurImageChannel',
           'DecoderThreadSupport', 'ReadPolicyRights',
           'GrayscaleType', 'DestroySplayTree',
           'CopyBlackCompositeOp', 'UndefinedException', 'ShaveImage',
           'SetXMLTreeAttribute', 'RelinquishSemaphoreInfo',
           'MagickExtentImage', 'ImageInfoRegistryType',
           'PixelGetGreen', 'MagickDecipherImage', 'DrawBezier',
           'OrderedDitherImage', 'EnhanceImage', 'RedQuantum',
           'HashStringType', 'MinMaxStretchImage', 'LongPixel',
           'SyncCacheViewPixels', 'PercentValue',
           'ChopPathComponents', 'DrawSetStrokeColor',
           'GetPseudoRandomValue', 'AnyStyle', 'QuantizationError',
           'ConcatenateMode', 'ScaleImage', 'PlusCompositeOp',
           'ClonePixelView', 'MagickChopImage', 'StreamError',
           'FillToBorderMethod', 'SetMagickInfo',
           'MagickGetImageTicksPerSecond', 'ScreenCompositeOp',
           'ModifyImage', 'SubimagePath', 'AutoGammaImage',
           'TopHatMorphology', 'MagickGetImageChannelFeatures',
           'DoublePixel', 'MagickRollImage', 'MagickGetQuantumDepth',
           'TransformImageColorspace', 'GetMagickReleaseDate',
           'PixelSetIndex', 'BicubicInterpolatePixel', 'DrawLine',
           'SpliceImageList', 'IsGeometry', 'GetCacheViewException',
           'DrawPathCurveToAbsolute', '_ColorPacket', 'ChannelType',
           'MagickEnhanceImage', 'MagickSelectiveBlurImage',
           'TransformImage', 'SetQuantumImageType', 'ShadeImage',
           'ResetTimer', 'GetImageList', 'CornersKernel',
           'GetLocaleOptions', 'MagickLocaleOptions',
           'MagickSketchImage', 'BohmanFilter', 'GetQuantumType',
           'OpenMagickStream', 'CycleColormapImage',
           'LaplacianKernel', 'ExclusionCompositeOp',
           'GetCacheViewExtent', 'MagickTransposeImage',
           'UndefinedJoin', '_DelegateInfo', 'NorthGravity',
           'YIQColorspace', 'MagickLevelImageChannel',
           'SetImageAlphaChannel', 'PixelGetFuzz', 'BlobError',
           'SentinelDistortion', 'DestroyStringInfo', 'DrawColor',
           'MagickEvaluateOptions', 'EncodeImageHandler',
           'LoadMimeLists', 'RenderingIntent', 'ArcDistortion',
           'MagickGetImageScene', 'ConfigureFatalError',
           'GetMagickRegistry', 'GetColorInfoList', 'AcquireImage',
           'DoGKernel', 'MagickProgressMonitor', 'SetImageColorspace',
           'PeakAbsoluteErrorMetric',
           'MagickSetImageCompressionQuality', 'GetMagickProperty',
           'DrawSetStrokeLineJoin', 'MagickMatteFloodfillImage',
           'LocaleNCompare', 'DrawPushClipPath',
           'MagickResourceOptions', 'DoublePixelPacket',
           'ColorBurnCompositeOp', 'DstCompositeOp',
           'MagickBlackThresholdImage', 'CloseMorphology',
           'BilevelImage', 'FrameMode', 'CMYKQuantum', 'QuantizeInfo',
           'ColorDodgeCompositeOp', 'CoderComponentTerminus',
           'NewDrawingWand', 'MagickSetImageFilename',
           'DefaultChannels', 'ResetHashmapIterator',
           'GetMagickHomeURL', 'BilinearInterpolatePixel',
           'ConcatenateColorComponent', 'IsSubimage', 'BevelJoin',
           'MathematicsCompositeOp', 'MagickFilterImageChannel',
           'GetOneAuthenticPixel', 'SetRandomKey', 'PolicyDomain',
           'MimeComponentTerminus', 'DrawResetVectorGraphics',
           'ContinueTimer', 'ResourceLimitError',
           'PixelGetCurrentIteratorRow', 'BlobEvent',
           'MagickSetImageCompose', 'SaturationPreview',
           'GetConfigureBlob', 'MagickSetImageMatte',
           'RemoveZeroLayer', 'PixelSetFirstIteratorRow',
           'GetExceptionMessage', 'GetImageChannelDistortion',
           'PreviousDispose', 'MagickColorDecisionListImage',
           'MagickCompositeImageChannel', 'GammaPreview',
           'LogEventType', 'RemoveImageFromList', 'ConstantString',
           'DestroyQuantumInfo', 'GetCacheViewVirtualPixels',
           'AffineTransformImage', 'MagicComponentGenesis',
           'TintImage', 'ListModuleInfo', 'FxImageChannel',
           'UndefinedTransmitType', 'EdgesKernel', 'ExceptionInfo',
           'XServerWarning', 'ColorPacket',
           'MagickRegionOfInterestImage',
           'RemoveElementByValueFromLinkedList',
           'GetConfigureInfoList', 'CoderError', 'CompositeImage',
           'GetMagickQuantumDepth', 'DrawGradientImage',
           'MagickAutoGammaImageChannel', 'GetAffineMatrix',
           'SplayTreeInfo', 'AllValidate', 'ColorSeparationMatteType',
           'Rec601YCbCrColorspace', 'MagickSetImageScene',
           'LongPixelPacket', 'PointInfo', 'CoderComponentGenesis',
           'SquareCap', 'MontageInfo', 'NewPixelView',
           'DefineImageRegistry', 'GetMimeType', 'DelegateFatalError',
           'DestroyDrawingWand', 'AbsoluteIntent',
           'MogrifyImageCommand', 'DrawGetTextInterwordSpacing',
           'MagickPingImage', 'AppendImageToList',
           'WhiteVirtualPixelMethod', 'SetImageInfoProgressMonitor',
           'MagickSetPage', 'SelectiveBlurImage', 'SetQuantumQuantum',
           'GrayscalePreview', 'OptimizePlusLayer', 'PolarDistortion',
           'GetNextImageAttribute', 'MagickGetImagePage',
           'NewPixelRegionIterator', 'DirectionType', 'WelshFilter',
           'MagickAdaptiveBlurImageChannel', 'LiquidRescaleImage',
           'DeactivateAlphaChannel', 'DestroySemaphoreInfo',
           'MagickQueryConfigureOptions', 'MagickGaussianBlurImage',
           'DrawGetFontSize', 'ImageType', 'SoftLightCompositeOp',
           'NoCompression', 'MagickTintImage',
           'UnsharpMaskImageChannel', 'DestroyImage',
           'GetXMLTreeContent', 'ConvertHSLToRGB',
           'GetDelegateInfoList', 'RootMeanSquaredErrorMetric',
           'MagickTrimImage', 'AddValueToSplayTree',
           'DefineImageOption', 'SetPixelCacheVirtualMethod',
           'ThumbnailImage', 'MagickDeleteOption', 'MaximumImages',
           'SeedPseudoRandomGenerator', 'ListConfigureInfo',
           'MagickListOptions', 'ScaleResampleFilter',
           'PersistPixelCache', 'MagickSetImageGamma',
           '_SplayTreeInfo', 'OilPaintPreview',
           'DrawSetVectorGraphics', 'BlurPreview', 'DelegateError',
           'WriteMode', 'FillRule', 'GetPixels',
           'MagickDitherOptions', 'IsMagickOption', 'MagickSetType',
           'GetPathComponent', 'GetNumberOfNodesInSplayTree',
           'MagickTransformImage', 'MagickFxImage',
           'MagickLogOptions', 'PixelGetMagentaQuantum',
           'LocaleComponentGenesis', 'UserDefinedKernel', 'ImageInfo',
           'AddNoiseImageChannel', 'Pxr24Compression',
           'GetAuthenticIndexQueue', 'AcquireTimerInfo',
           'SetClientName', 'GetPixelViewWand', 'WriteImages',
           'FloodfillMethod', 'MagickSetGravity', 'ConvexHullKernel',
           'DeprecateEvent', 'BlobWarning', 'GetPixelViewY',
           'NoCompositeOp', 'MagentaQuantum', 'UndefinedSpread',
           'MagickWandGenesis', 'AcquireUniqueSymbolicLink',
           'UndefinedFunction', 'OrderedPosterizeImageChannel',
           'DestroyImageList', 'GetXMLTreeAttributes',
           'UserSpaceOnUse', 'DiamondKernel', 'WritePolicyRights',
           'TransformRGBImage', 'GetOneVirtualPixel',
           'MagickGetImageRenderingIntent', 'LogComponentGenesis',
           'MagickAdaptiveBlurImage', '_QuantizeInfo',
           'PaintOpaqueImageChannel', '_MimeInfo', 'PixelSetBlack',
           'DrawGetStrokeColor', 'GravityType',
           'BlackVirtualPixelMethod', 'ExpandedStretch',
           'PlaneInterlace', 'DrawSetClipUnits',
           'MagickResetIterator', 'GetNextValueInLinkedList',
           'SteganoImage', 'MagickGammaImageChannel', 'StyleType',
           '_StringInfo', 'MagickOpaqueImage', 'NoneDispose',
           'DrawSetTextKerning', 'BartlettFilter',
           'MagickSolarizeImage', 'ResetSplayTreeIterator',
           'MagickGetImageDispose', 'GetCacheViewStorageClass',
           'UnshiftImageList', 'RelinquishMagickMemory',
           'SetCacheViewVirtualPixelMethod', 'UndefinedNoise',
           'MagickSharpenImageChannel', 'AllEvents',
           'GetImageChannelDistortions', 'CacheView',
           'RegistryComponentGenesis', 'DrawSetStrokePatternURL',
           'DullPreview', 'ChromaticityInfo', 'SpiffPreview',
           'DrawAnnotation', 'MagickGetImageChannelExtrema',
           'MagickBooleanOptions', 'UndefinedRegistryType',
           'SampleImage', 'UndefinedValidate', 'SentinelFilter',
           'DrawSetFillColor', 'HSLColorspace', 'ErrorHandler',
           'IsMagickInstantiated', 'SetImagePixels',
           'CloseIntensityMorphology', 'YCbCrColorspace',
           'RightBottomOrientation', 'DespeckleImage',
           'MagickLayerOptions', 'CloneImageProfiles',
           'GetLastValueInLinkedList', 'SetCacheViewStorageClass',
           'DrawPopPattern', 'LevelImage', 'AtopCompositeOp',
           '_StopInfo', 'RemoveImageRegistry', 'AcquireNextImage',
           'ThrowMagickException', 'MagickDescribeImage',
           'MagickVignetteImage', 'InverseFourierTransformImage',
           'InvokeDynamicImageFilter', 'UpdatePixelViewMethod',
           'DestroyPixelView', 'GetImageTotalInkDensity',
           'MagickSetImageCompression', 'ResetImageOptions',
           'RGBQuantum', 'RelativeIntent',
           'MagickBrightnessContrastImage', 'PlasmaImage',
           'MagickPath', 'PsiValue', 'PaintTransparentImage',
           'MagickNormalizeImage', 'CanonicalXMLContent',
           'CompositeValidate', 'PixelSetBlue',
           'MultiplicativeNoiseEvaluateOperator',
           'ForwardFourierTransformImage', 'MagickRadialBlurImage',
           'ExcerptImage', 'MagickSetSizeOffset', 'PixelView',
           'SetImageProperty', 'MagickReadImageFile',
           'MagickFloodfillPaintImage', 'PixelGetRed',
           'YellowChannel', 'CompareSplayTreeStringInfo',
           'MagickGetImageChannelKurtosis', 'FileToString',
           'StoppedTimerState', 'PaintFloodfillImage',
           'GetLocaleMessage', 'ConvolveImageChannel', 'MatteChannel',
           'DrawRectangle', 'LinePrimitive', 'XGetImportInfo',
           'SemaphoreInfo', 'MagickBooleanType',
           'GetBlobStreamHandler', 'FormatMagickString',
           'GaussJordanElimination', 'DestroyBlob',
           'MagickSetImageColor', '_AffineMatrix',
           'GetVirtualPixelQueue', 'PerceptualIntent',
           'EdgeVirtualPixelMethod', 'ArcsinFunction',
           'MagickSeparateImageChannel', 'GetImageType',
           'DrawSetStrokeLineCap', 'ExtendedSignedIntegralType',
           'StretchType', 'SystemPolicyDomain',
           'MagickGetImageColors', 'DestroyTimerInfo',
           'ClipPathImage', 'NorthEastGravity', 'BlurKernel',
           'OHTAColorspace', 'LZWCompression', 'MeanEvaluateOperator',
           'DrawPathLineToHorizontalAbsolute', 'UndefinedPrimitive',
           'MagickTransformImageColorspace', 'UndefinedPolicyRights',
           'DrawGetBorderColor', 'CMYColorspace', 'AnnotateImage',
           '_MagickPixelPacket', 'XValue',
           'MagickGetImageOrientation', 'SouthWestGravity',
           'DrawSetFontWeight', 'IdentifyValidate',
           'HaldClutImageChannel', 'PosterizeImage',
           'MagickMorphImages', 'BGRAQuantum', 'UndefinedQuantum',
           'N11__mbstate_t3DOT_2E', 'MagickRandomThresholdImage',
           'MagickSetImageClipMask', 'ConvolveImage',
           'AndEvaluateOperator', 'GetImageMean',
           'LinearLightCompositeOp', 'ImageToBlob', 'SetImageList',
           'GetImageChannelKurtosis',
           'MagickGetImageCompressionQuality', 'BlueQuantum',
           'MagickRandomThresholdImageChannel', 'LocaleInfo',
           'BarycentricColorInterpolate', 'ClassType',
           'DestroyDrawInfo', 'ReplaceCompositeOp',
           'DestroyImagePixels', 'FilterFatalError',
           'ImpulseNoiseEvaluateOperator', 'MagickSetImageType',
           'MogrifyImage', 'DrawEllipse',
           'ResetImageArtifactIterator', 'IndexChannel',
           'MagickNegateImageChannel', 'NewSplayTree',
           'MagickMontageImage', 'MagickDirectionOptions',
           'IdentityAffine', 'ConvertHSBToRGB', 'MagickWand',
           'MagickGetImageSize', 'EndianType',
           'MagickGetImageChannelRange', 'MagickBlueShiftImage',
           'TrimBoundsLayer', 'FloatPixel', 'RGBAQuantum',
           'DrawGetFillAlpha', 'EncipherImage', 'RightAlign',
           'GetQuantumPixels', 'ImageWarning', 'ImplodeImage',
           'GetImageIndexInList', 'ReadStream', 'ExplicitFormatType',
           'MagickAdaptiveResizeImage', '_Ascii85Info',
           'MagickGetImageProfiles', 'RandomThresholdImage',
           'CbYCrAQuantum', 'DrawSetTextUnderColor',
           'RemoveImageOption', 'SetStringInfo',
           'MagickEndianOptions', 'XServerFatalError',
           'MagickGetImageChannelMean', 'RandomComponentGenesis',
           'DrawGetTextEncoding', 'GetPixelViewPixels',
           'GetNextXMLTreeTag',
           'DrawPathCurveToQuadraticBezierSmoothAbsolute',
           'MagickCoderOptions', 'MagickSetInterpolateMethod',
           'GetPreviousImageInList', 'OpenModule', 'GetDelegateList',
           'PeakSignalToNoiseRatioMetric', 'DivideCompositeOp',
           'AcquireSemaphoreInfo', 'MagickHasPreviousImage',
           'MagickComponentTerminus', 'MagickHaldClutImage',
           'MagickLiquidRescaleImage', 'GetLocaleInfo_',
           'DestroyResampleFilter', 'PrewittKernel', 'ButtCap',
           'LessValue', 'MagickSwirlImage', 'SyncChannels',
           'OverlineDecoration', 'PolicyRights', 'IsOpacitySimilar',
           'GetOptimalKernelWidth1D', 'DrawPathStart',
           'DestroyCacheView', 'MagickGetImageChannelDistortions',
           'MagickGetVersion', 'MagickPixelPacket', 'AutoLevelImage',
           'DuplexTransferPixelViewIterator', 'HuePreview',
           'ConvertRGBToHWB', 'ResolutionType', 'GetNumberColors',
           'ErrorException', 'DrawClipPath', 'GravityAdjustGeometry',
           'MagickError', 'UserEvent', 'MagickInterpolateOptions',
           'MagickGetHomeURL', 'ThrowException',
           'MagickWriteImageBlob', 'GreenChannel',
           'GetCacheViewAuthenticPixels', '_Timer', 'DrawCircle',
           'BrightnessPreview', 'MagickRaiseImage',
           'DrawSetStrokeWidth', 'HWBColorspace',
           'ThrowMagickExceptionList', 'DestroyImageInfo',
           'LuminizeCompositeOp', '_TokenInfo', '_PrimaryInfo',
           'PixelSetColorCount', '_ResampleFilter',
           'PixelGetIteratorExceptionType', 'MagickLayerMethod',
           'MagickModulateImage', 'GetMagicInfo', 'PseudoClass',
           'SeparateImageChannel', '_LinkedListInfo', 'PolaroidImage',
           'PadSpread', 'MagickGetSize', 'FunctionImage',
           'CloneKernelInfo', 'MagickSetOrientation', 'Timer',
           'EmbossImage', 'MagickClutImage', 'GetClientPath',
           'DrawSetFontStyle', 'AssociatedQuantumAlpha',
           'MagickMimeOptions', 'MagickGetImageMatte',
           'MagickGetImageFilename', 'GetConfigureValue',
           'ResourcePolicyDomain', 'ClonePixelWand', 'SetImageMask',
           'MagickGetCopyright', 'ConfigureEvent',
           'MagickColorOptions', 'LeftShiftEvaluateOperator',
           'AlignType', 'CompareImageChannels', 'CompressionType',
           'MemoryResource', 'RadialBlurImage', 'SubstituteString',
           'UnityKernel', 'AcquireCacheViewIndexes',
           '_ImageAttribute', 'MagickGetImageRange',
           'RegistryComponentTerminus', 'MagickTypeOptions',
           'IsMagickConflict', 'ColorspaceType', 'GetModuleList',
           'ExtensionPath', 'FormatMagickTime', 'IsGrayImage',
           'ModuleWarning', 'MagickEvaluateImageChannel',
           'AdaptiveThresholdImage', 'PathPolicyDomain',
           'InjectImageBlob', 'SetMonitorHandler',
           'MagickTransparentImage', 'DisposeImages',
           'PostscriptGeometry', 'DitherMethod', 'DrawSkewY',
           'DrawSkewX', 'MagickWriteImage', 'ConfigureInfo',
           'AddPathToXMLTree', 'CompareStringInfo',
           'MagickMethodOptions', 'MagickComposeOptions',
           'KernelInfo', 'OptimizeImageLayers', 'DeleteImageArtifact',
           'DistortImageMethod', 'AffineProjectionDistortion',
           'MagickGetQuantumRange', 'MagickClampImage', '_MagickWand',
           'BackgroundAlphaChannel', 'OptimizeImageLayer',
           'SetQuantumAlphaType', 'ReplaceImageInList',
           'MagickSetAntialias', 'GetMagickInfoList',
           'MagickFilterImage', 'FxImage', 'DrawPushPattern',
           'DrawPathMoveToRelative', 'DrawPathEllipticArcRelative',
           'DrawSetStrokeAntialias', 'MagickGetImage',
           'PerspectiveProjectionDistortion', 'PixelSetAlphaQuantum',
           'TransferPixelViewIterator', 'SetImageChannelDepth',
           'GetMagicName', 'SinusoidFunction',
           'MagickGetImageCompose', 'CatchImageException',
           'DrawGetStrokeMiterLimit', 'BilevelImageChannel',
           'CbYCrQuantum', 'ListMagickOptions', 'BlurCompositeOp',
           'SetImageProgressMonitor', 'GetImageRange',
           'IsMagickColorSimilar', 'SetEvaluateOperator',
           'PixelSetColor', 'QuantizeImage', 'DrawArc',
           'MagickCompositeImage', 'GetQuantumExtent',
           'InCompositeOp', 'PixelSetMagickColor', 'UndefinedPath',
           'ReadInlineImage', 'LevelColorsImage', 'DrawContext',
           'PixelGetOpacityQuantum', 'CloneMemory',
           'DestroyPixelWands', 'CompareSplayTreeString',
           '_SegmentInfo', 'AlphaQuantum',
           'MagickGetImageBackgroundColor', 'GetPolicyValue',
           'ResetSplayTree', 'GetMagickResource',
           'MagickGetImageWidth', 'ConfigureComponentTerminus',
           'NoiseType', 'LineJunctionsKernel', 'ResizeMemoryHandler',
           'CorruptImageError', 'ExtractAlphaChannel',
           'MagickClampImageChannel', 'ExtentImage',
           'QueueCacheViewAuthenticPixels', 'EdgeOutMorphology',
           'DstAtopCompositeOp', 'SetImageType', 'MagentaChannel',
           'CopyCompositeOp', 'ImageFilterHandler',
           'TopLeftOrientation', 'YUVColorspace',
           'MagickGetImageDepth', 'MagickSetLastIterator',
           'GetCacheViewVirtualPixelQueue', 'SketchImage',
           'GetMagickQuantumRange', 'MagickGetCompressionQuality',
           'MagickEvaluateImage', 'MagickReadImageBlob',
           'SyncAuthenticPixels', 'BlobToFile',
           'GetNextKeyInSplayTree', 'DestroyThresholdMap',
           'ExtraExpandedStretch', 'MagickAppendImages',
           'ResetImageAttributeIterator', 'ConfigureWarning',
           'MagickQuantizeImage', 'MagickRelinquishMemory',
           'MagickAlphaOptions', 'GetEnvironmentValue',
           'MagickFlipImage', 'DestroyPixelIterator',
           'MaskVirtualPixelMethod', 'IndexAlphaQuantum',
           'ListLocaleInfo', 'MagickCommand', 'PrimaryInfo',
           'AllocateImage', 'MagickEqualizeImage', 'CompareValidate',
           'SetImageExtent', 'GetMagickVersion', 'XMLTreeInfoToXML',
           'GetImageProperty', 'QuantumAny', 'DrawSetTextAntialias',
           'CondensedStretch', 'MonitorFatalError', 'ListColorInfo',
           'StringInfoToHexString', 'ParzenFilter',
           'MagickSparseColorOptions', 'PixelSetOpacityQuantum',
           'PixelGetRedQuantum', 'GetImageAlphaChannel',
           'ParsePageGeometry', 'UndefinedOrientation',
           'ListPolicyInfo', 'MagickThresholdOptions', 'X11Event',
           'UnlockSemaphoreInfo', 'ResetMethod',
           'PixelSetYellowQuantum', 'GetValueFromHashmap',
           'MagickDeconstructImages', 'MagickGetImageLength',
           'DrawMatte', 'GetLocaleExceptionMessage',
           'MagickUndefinedOptions', 'SemiExpandedStretch',
           'DestroyModuleList', 'MontageImageList', 'LineInterlace',
           'GrayAlphaQuantum', 'DeleteImageOption', 'ModuleInfo',
           'MagickColorizeImage', 'SetImageColor', 'LSBEndian',
           'Base64Encode', 'PixelSetRedQuantum', 'MagickFatalError',
           'MagickGetImageColorspace', 'MagickGetException',
           'MotionBlurImage', 'ExecutePolicyRights', 'CompareImages',
           'DecipherImage', 'BlobFatalError', 'MagickProfileImage',
           'SetImageProfile', 'DXT5Compression',
           'MagickAnnotateImage', 'AbsoluteErrorMetric',
           'MagickDestroyImage', 'IntegerPixel', 'ListDelegateInfo',
           'MagickStorageOptions', 'AlphaChannel',
           'MagickCommentImage', 'NoEvents',
           'MagickNormalizeImageChannel', 'CompositeOperator',
           'PingBlob', 'MagickSetInterlaceScheme',
           'CompositeImageCommand', 'DrawGetFillColor',
           'MagickRecolorImage', 'QuantumPixel',
           'MagickSelectiveBlurImageChannel', 'MagickGetFormat',
           'BesselFilter', 'GetPixelViewException', 'ZoomImage',
           'MiterJoin', 'SparseColorImage', 'PixelSetQuantumColor',
           'RemoveNodeByValueFromSplayTree', 'GetImageExtrema',
           'BlendCompositeOp', 'SetImageVirtualPixelMethod',
           'MergeLayer', 'GetThresholdMap', 'DistortImage',
           'SincFilter', 'MagickCombineImages', 'GetPageGeometry',
           'StringRegistryType', 'MagickConvolveImage',
           'DestroyLocaleOptions', 'MagickSetIteratorIndex',
           'CompositeLayer', 'MagickSetImageColorspace',
           'GetValueFromLinkedList', 'RightShiftEvaluateOperator',
           'DrawGetGravity', 'DrawPathEllipticArcAbsolute',
           'ColorInfo', 'OpaqueAlphaChannel', 'FuzzyColorCompare',
           'SrcCompositeOp', 'InterpretImageFilename',
           'LogMagickEventList', 'UndefinedPolicyDomain',
           'UndefinedEvaluateOperator', 'MagickGetImageChannelDepth',
           'ssize_t', 'CMYKAQuantum', '_ChannelFeatures',
           'MagickGetImageTotalInkDensity', 'QueryColorname',
           'GetRandomKey', 'MagickSetPointsize',
           'MagickConfigureOptions', 'MagickDeleteImageArtifact',
           'PruneTagFromXMLTree', 'MagickMapImage',
           'DrawPeekGraphicWand', 'PerspectiveDistortion',
           'DuplicateBlob', 'EuclideanKernel',
           'UndefinedColorInterpolate', 'MagickDespeckleImage',
           'TransparentImage', 'Rec601LumaColorspace', 'EdgeImage',
           'IsPaletteImage', 'DuplexTransferPixelViewMethod',
           'B44Compression', 'KaiserFilter', 'GetXMLTreeTag',
           '_ElementReference', 'BackgroundDispose',
           'MagickQueryConfigureOption', 'ImageFatalError',
           'ValidateColormapIndex', 'MagickSetImageBorderColor',
           'MagickFormatType', 'ListFiles', 'MSBEndian',
           '_ChromaticityInfo', 'MagickChannelOptions',
           'MagickGetImageBlob', 'MagickAutoGammaImage', 'DrawAffine',
           'GrayPadQuantum', 'LevelizeImage',
           'AsynchronousResourceComponentTerminus', 'DrawSetGravity',
           'GetNextValueInHashmap', 'DrawComposite', 'MagickGetPage',
           'IsImageObject', 'LogInfo', 'DiskKernel',
           'UndefinedCompression', 'GetBlobError', 'DrawPatternPath',
           'PartitionInterlace', 'PingImages',
           'DrawPathCurveToQuadraticBezierSmoothRelative',
           '_TypeInfo', 'SineEvaluateOperator', 'MagickCharcoalImage',
           'OverCompositeOp', 'MapMode', 'VividLightCompositeOp',
           'WidthValue', 'MagickClutImageChannel', 'ExpandFilename',
           'MagickPosterizeImage', 'RotateImage',
           'GetMimeDescription', 'GetImageProfile', 'PointPrimitive',
           'MagickStereoImage', 'ChannelThresholdImage',
           'EvenOddRule', 'GetXMLTreeProcessingInstructions',
           'CanonicalPath', 'JPEGCompression',
           'MagickGetExceptionType', 'CloseCacheView',
           'CompareImageCommand', 'MagickSetImageProperty',
           'UndefinedDirection', 'DrawSetBorderColor',
           'RemoveZeroDelayLayers', 'SetGeometryInfo', 'IsGlob',
           'ImplicitFormatType', 'HaldClutImage', 'UndefinedAlign',
           'CharcoalDrawingPreview', 'OrderedDitherImageChannel',
           'RectangleInfo', 'DestroyMontageInfo', 'MagickCoreGenesis',
           'ChiValue', 'ValidateType', 'PolicyError', 'RaisePreview',
           'NoThreadSupport', 'MagickCompareImageLayers',
           'GetNextValueInSplayTree', 'OpaquePaintImageChannel',
           'PNGInterlace', 'DrawGetFillOpacity', 'MagickDisplayImage',
           'IsOpaqueImage', 'MagickSetSize', 'DXT3Compression',
           'MagickPingImageBlob', 'GetVirtualPixels',
           'ThresholdPreview', 'ResetStringInfo',
           'MagickResampleImage', 'Ascii85Initialize',
           'DrawGetFontStyle', 'PolicyComponentGenesis',
           'Ascii85Flush', 'AcquireStringInfo', 'MagickToMime',
           'ResetAlphaChannel', 'LinearBurnCompositeOp',
           'DeleteImageFromList', 'RemoveElementFromLinkedList',
           'GetImageArtifact', 'ListMagickInfo', 'ResamplePixelColor',
           'MagickFlopImage', 'DrawEvent', 'SmoothMorphology',
           'ResourceEvent', 'ImportQuantumPixels', 'PolicyWarning',
           'RemoveImageArtifact', 'PinLightCompositeOp',
           'NoDitherMethod', 'WandFatalError', 'MagickGetImageUnits',
           'RemoveFirstImageFromList', 'GetNextImageInList',
           'MagickGetImageExtrema', 'BrightnessContrastImageChannel',
           'MagickCoalesceImages', 'SystemCommand', 'ReplaceMethod',
           'PreviewImage', 'GetCacheViewColorspace',
           'MagickSetImageProgressMonitor', 'DestroyRandomInfo',
           'SetImage', 'BumpmapCompositeOp', 'CompareHashmapString',
           'GetQuantizeInfo', 'SetStringInfoDatum',
           'GetImageListSize', 'RectangleKernel',
           'CorrelateNormalizeValue', 'UndefinedMorphology',
           'IsBlobSeekable', 'MagickSetImageAttribute',
           'MinEvaluateOperator', 'GetUserTime', 'DrawPolyline',
           'CloneString', 'MagickConstituteImage', 'PrimitiveInfo',
           'MagickOffsetType', 'MagickSetImageGravity',
           'SetExceptionInfo', 'AcquireUniqueFileResource',
           'MagickFunction', 'ClipPathUnits', 'PointMethod',
           'SetImageInfo', 'CloneImageList', 'ReduceNoisePreview',
           'FormatImageProperty', 'PixelSetCyan',
           'AcquireQuantumMemory', 'MagickShadowImage',
           'SpreadMethod', 'TransparentAlphaChannel',
           'UndefinedPixel', 'GetPathAttributes', 'NewImageList',
           'ClipImagePath', 'GetNextImageArtifact', 'SimilarityImage',
           'XImportInfo', 'DrawClearException', 'GrayChannel',
           'MagickContrastImage', 'GetImageFromList',
           'PowEvaluateOperator', 'ConjureImageCommand',
           'LagrangeFilter', 'FlattenImages', 'ThickenMorphology',
           'MagickReadImage', 'ElementReference',
           'NegateImageChannel', 'MagickGetImageCompression',
           'MagickContrastStretchImage', 'PixelSetLastIteratorRow',
           'GetDrawInfo', 'CbYCrYQuantum', 'ConcatenateMagickString',
           'LinearGradient', 'MagickHasNextImage',
           'UniqueImageColors', 'ListTypeInfo', 'Group4Compression',
           'ConstituteComponentGenesis', 'MagickIncarnate',
           'MagickForwardFourierTransformImage', 'CharcoalImage',
           'GetMagickRawSupport', 'DrawRotate', 'OptionFatalError',
           'CloneImageOptions', 'LZWEncodeImage', 'UndefinedStyle',
           'FilterInterpolatePixel', 'BlobTransmitType',
           'SwirlPreview', 'CopyOpacityCompositeOp',
           'AcquireOneMagickPixel', 'DrawPathFinish',
           'MagickGetImageFuzz', 'CloneDrawInfo',
           'ColorFloodfillImage', 'OptionError', 'SyncImageList',
           'GetMagickPackageName', 'GetXMLTreeOrdered',
           'GetImageEncoder', 'MagickClipImagePath',
           'NewPixelIterator', 'ThresholdEvaluateOperator',
           'DestroyLinkedList', 'MagickGaussianBlurImageChannel',
           'GetMagickGeometry', 'MagickGetImageDelay',
           'GetImageReferenceCount', 'UndefinedFormatType',
           '__ssize_t', '_BlobInfo', 'ContrastStretchImage',
           'LosslessJPEGCompression', 'MagickGetPointsize',
           'CopyAlphaChannel', 'AddModulusEvaluateOperator',
           'MagickGetOrientation', 'UltraExpandedStretch',
           'GetOneVirtualMethodPixel', '_GeometryInfo',
           'BilinearForwardDistortion', 'GetOptimalKernelWidth2D',
           'MagickRotateImage', 'StreamTransmitType',
           'MagickFxImageChannel', 'MagickGetPackageName',
           'LineThroughDecoration', 'MagickPaintFloodfillImage',
           'MagickCompareImages', 'PopImagePixels', 'DelegateWarning',
           'MultiplyCompositeOp', 'MagickGetImageAlphaChannel',
           'DrawGetTextAntialias', 'AcquireResampleFilter',
           'UndefinedQuantumFormat', 'GaussianBlurImageChannel',
           'ConstantVirtualPixelMethod', 'ShearPreview',
           'OptimizeTransLayer', 'MagickAddImage',
           'GetMonitorHandler', 'ExtraCondensedStretch',
           'MagickPaintTransparentImage', 'GetDelegateCommands',
           'MagickResetImagePage', 'DeleteMagickRegistry',
           'InsertValueInLinkedList', 'DrawGetFillRule',
           'CompareImageLayers', 'FloodfillPaintImage',
           'MagickThresholdImage', 'MogrifyImageInfo',
           'PolynomialDistortion', 'UnsignedQuantumFormat', 'LineCap',
           'MagickPaintOpaqueImage', 'ResetImagePage',
           'SetQuantumScale', 'LinearStretchImage',
           'MagickMotionBlurImage', 'RelinquishMagickResource',
           'GetImageInfo', 'NewXMLTreeTag',
           'MagickGetImageDistortion', 'CacheError', 'TimeResource',
           '_DrawingWand', 'SrcOutCompositeOp',
           'MimeComponentGenesis', 'AcquireUniqueFilename',
           'TypeError', 'RollPreview', 'OilPaintImage',
           'DXT1Compression', 'GetImageQuantizeError', 'MagnifyImage',
           'TrimImage', 'BezierPrimitive', 'DrawGetTextUnderColor',
           'MontageValidate', 'GetImageChannelMean', 'RegistryType',
           'GetRandomValue', 'ClonePixelIterator',
           'MultiplicativeGaussianNoise', 'LogMagickEvent',
           '_PixelPacket', 'ExpandFilenames', 'DestroyMemoryHandler',
           'DrawSetStrokeOpacity', 'DilateIntensityMorphology',
           'MagickSetImageAlphaChannel',
           'MagickUnsharpMaskImageChannel', 'ListMimeInfo',
           'GetTypeInfo', 'MagickClipImage', 'PixelSetBlueQuantum',
           'MosaicImages', 'MagickFilterOptions',
           'ImportImageCommand', 'GetBlobFileHandle',
           'MagickWaveImage', 'SetErrorHandler', 'SetResampleFilter',
           'MagickWarning', 'TailPath', 'MagickAverageImages',
           'MinimumValue', 'SemaphoreComponentGenesis',
           'AutoLevelImageChannel', 'LinkedListInfo', 'HammingFilter',
           'DestroyConfigureOptions', 'PixelGetAlpha',
           'GetImageChannelExtrema', 'DisplayImages',
           'GetValueFromSplayTree', 'TrueAlphaChannel',
           'YellowQuantum', 'MagickSetImageWhitePoint',
           'RandomVirtualPixelMethod', 'WavePreview',
           'GetConfigureOption', 'MagickDrawImage', 'IsImageSimilar',
           'MagickQueryFormats', 'ImpulseNoise', 'MonitorHandler',
           'MinifyImage', 'PixelIteratorGetException',
           'LocaleCompare', 'MagickOrderedPosterizeImage',
           'MagickOption', 'DrawSetStrokeDashOffset',
           'PixelGetExceptionType', 'BlueChannel',
           'DisplayImageCommand', 'IndexPacket', 'UndefinedMode',
           'NewMagickWandFromImage', 'CopyYellowCompositeOp',
           'LeftTopOrientation', 'RegisterStaticModules',
           'GetConfigureList', 'MagickGetResource',
           'MagickFunctionOptions', 'DisassociatedQuantumAlpha',
           'DestroyImageAttributes', 'RLECompression',
           'ListThresholdMaps', 'NormalizeImageChannel',
           'TransposeImage', 'EdgeMorphology', 'GetImageMagick',
           'InterlaceType', 'AlphaChannelType',
           'MagickAutoLevelImageChannel',
           'GetPixelCacheVirtualMethod', 'PathPrimitive',
           'IsEventLogging', '_ConfigureInfo', 'MagickPreviewOptions',
           'RGBPadQuantum', 'QuadraticFilter', 'PixelGetOpacity',
           'MatteFloodfillImage', 'MagickSetImageDispose',
           'NewLinkedList', 'UndefinedClass', 'GetStringInfoLength',
           'MagickGetImageProfile', 'DrawError', 'MagickMonitor',
           'DrawGetStrokeWidth', 'HuffmanDecodeImage',
           'MagickWriteImages', 'ConfigureComponentGenesis',
           'UndefinedReference', 'PixelGetIteratorException',
           'XServerError', 'MagickGetImageInterpolateMethod',
           'LinkedListToArray', 'MagickLineCapOptions', 'StringToken',
           'ClearMagickWand', 'HeadPath', 'MagickPreviousImage',
           'DrawGetFontStretch', 'AnyStretch', 'FrameImage',
           'CharPixel', 'SetMagickPrecision',
           'ResetImagePropertyIterator', 'TrueColorType',
           'ClearPixelIterator', 'GetXMLTreeChild', 'RadialGradient',
           'MagickEncipherImage', 'DestroyImages', 'UnframeMode',
           'FileTransmitType', 'CloneMagickWand',
           'DeleteNodeByValueFromSplayTree', 'MagickMaximumImages',
           'MagickGetCompression', 'GetDelegateThreadSupport',
           'MagickRemapImage', 'OffsetInfo', 'PixelResetIterator',
           'MagickSetImagePixels', 'CloneStringInfo', 'UndefinedType',
           'ThinDiagonalsKernel', 'ColorDecisionListImage',
           'AcquireMemory', 'NoValidate', 'NoInterlace',
           'FileOpenError', 'IsTaintImage', 'UndefinedLayer',
           'CopyMagentaCompositeOp', 'TypeMetric',
           'GetImageChannelStatistics', 'GreaterValue',
           'AcquireCacheView', 'GetCacheViewAuthenticPixelQueue',
           'IsSceneGeometry', 'MagickSetImageVirtualPixelMethod',
           'HorizontalTileVirtualPixelMethod', 'MagickEvaluateImages',
           'ResampleFilter', 'MagickSetDepth', 'ThresholdImage',
           'DrawGetFontWeight', 'DrawSetFontSize', '_RandomInfo',
           'MagickDisplayImages', 'DrawSetFillAlpha', 'StringToList',
           'DrawSetClipPath', 'HermiteFilter', 'DisposeLayer',
           'MagickGetImagePixels', 'PixelGetNextIteratorRow',
           'IsPixelWandSimilar', 'StaticGravity', 'SetImageOption',
           'FormatsOnDiskValidate', 'LaplacianNoiseEvaluateOperator',
           'WarningHandler', 'MorphologyImageChannel',
           'HashStringInfoType', 'YNegative',
           'MagickGetInterpolateMethod', 'OptimizeImageTransparency',
           'SetResampleFilterInterpolateMethod', 'FormatStringList',
           'UndefinedCompositeOp', 'MagickQuantizeImages',
           'MapResource', 'MagickColorspaceOptions',
           'ThresholdImageChannel', 'PixelGetMagenta',
           '_LongPixelPacket', 'MagickAutoLevelImage', 'GetCoderInfo',
           'DrawPopGraphicContext', 'VignetteImage', 'StringInfo',
           'UndefinedGravity', 'DstOverCompositeOp',
           'MagickClipPathOptions', 'DefineImageProperty',
           'ImageAttribute', 'BottomHatMorphology',
           'ShepardsColorInterpolate', 'ConstituteComponentTerminus',
           'CloneCacheView', 'ModuleEvent', 'PixelGetNextRow',
           'IsColorSimilar']
