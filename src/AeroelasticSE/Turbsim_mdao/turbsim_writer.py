from turbsim_vartrees import turbsiminputs
from turbulence_spectrum import turb_specs
from wind_profile_writer import write_wind
class TurbsimBuilder(turbsiminputs):
    def __init__(self):
         self.turbsim_vt = turbsiminputs()
         self.tsim_input_file = 'turbsim_default.in'
         self.tsim_turbulence_file = 'turbulence_default.in'
         self.tsim_profile_file = 'default.shear'
 
         # Turbulence file parameters
         self.wind_speed = 8.
         self.L_u = 2.54e+02
         self.L_v=1.635e+02
         self.L_w=4.7e+01
         self.sigma_u=2.65e+00
         self.sigma_v=1.8e0
         self.sigma_w=1.525e0
         self.turbulence_file_name = 'tsim_user_turbulence_default.inp'
         self.turbulence_template_file = 'TurbsimInputFiles/turbulence_user.inp'
         
         # profile file parameters
         self.profile_tamplate = 'TurbsimInputFiles/shear.profile'
         self.shear_exponent = 0.2
         self.veer = 20
         self.turbsim_vt.metboundconds.ProfileFile = 'default.profile'

    def execute(self):

         # Write turbulence file
         turb_specs(V_ref=self.wind_speed, L_u=self.L_u, L_v=self.L_v, L_w=self.L_w, sigma_u=self.sigma_u,
                    sigma_v=self.sigma_v, sigma_w=self.sigma_w, filename=self.turbsim_vt.metboundconds.UserFile, template_file=self.turbulence_template_file)

         # Write profile file
         write_wind(V_ref=self.wind_speed, alpha=self.shear_exponent, Beta=self.veer, Z_hub=self.turbsim_vt.tmspecs.HubHt, filename=self.turbsim_vt.metboundconds.ProfileFile, template_file=self.profile_tamplate)

         tsinp = open(self.tsim_input_file, 'w')
         tsinp.write("-----\n")
         tsinp.write("-----\n")
         tsinp.write("-----\n")

         # runtime options
         tsinp.write("{}\n".format(self.turbsim_vt.runtime_options.echo))
         tsinp.write("{}\n".format(int(self.turbsim_vt.runtime_options.RandSeed1)))
         tsinp.write("{}\n".format(self.turbsim_vt.runtime_options.RandSeed2))
         tsinp.write("{}\n".format(self.turbsim_vt.runtime_options.WrBHHTP))
         tsinp.write("{}\n".format(self.turbsim_vt.runtime_options.WrFHHTP))
         tsinp.write("{}\n".format(self.turbsim_vt.runtime_options.WrADHH))
         tsinp.write("{}\n".format(self.turbsim_vt.runtime_options.WrADFF))
         tsinp.write("{}\n".format(self.turbsim_vt.runtime_options.WrBLFF))
         tsinp.write("{}\n".format(self.turbsim_vt.runtime_options.WrADTWR))
         tsinp.write("{}\n".format(self.turbsim_vt.runtime_options.WrFMTFF))
         tsinp.write("{}\n".format(self.turbsim_vt.runtime_options.WrACT))
         tsinp.write("{}\n".format(self.turbsim_vt.runtime_options.Clockwise))
         tsinp.write("{}\n".format(self.turbsim_vt.runtime_options.ScaleIEC))

         # Turbine/Model Specifications
         tsinp.write("\n")
         tsinp.write("----\n")
         tsinp.write("{}\n".format(self.turbsim_vt.tmspecs.NumGrid_Z))
         tsinp.write("{}\n".format(self.turbsim_vt.tmspecs.NumGrid_Y))
         tsinp.write("{}\n".format(self.turbsim_vt.tmspecs.TimeStep))
         tsinp.write("{}\n".format(self.turbsim_vt.tmspecs.AnalysisTime))
         tsinp.write("{}\n".format(self.turbsim_vt.tmspecs.UsableTime))
         tsinp.write("{}\n".format(self.turbsim_vt.tmspecs.HubHt))
         tsinp.write("{}\n".format(self.turbsim_vt.tmspecs.GridHeight))
         tsinp.write("{}\n".format(self.turbsim_vt.tmspecs.GridWidth))
         tsinp.write("{}\n".format(self.turbsim_vt.tmspecs.VFlowAng))
         tsinp.write("{}\n".format(self.turbsim_vt.tmspecs.HFlowAng))

         # Meteorological Boundary Conditions
         tsinp.write("\n")
         tsinp.write("----\n")
         tsinp.write("{}\n".format(self.turbsim_vt.metboundconds.TurbModel))
         tsinp.write("{}\n".format(self.turbsim_vt.metboundconds.UserFile))
         tsinp.write("{}\n".format(self.turbsim_vt.metboundconds.IECstandard))
         tsinp.write("{}\n".format(self.turbsim_vt.metboundconds.IECturbc))
         tsinp.write("{}\n".format(self.turbsim_vt.metboundconds.IEC_WindType))
         tsinp.write("{}\n".format(self.turbsim_vt.metboundconds.ETMc))
         tsinp.write("{}\n".format(self.turbsim_vt.metboundconds.WindProfileType))
         tsinp.write("{}\n".format(self.turbsim_vt.metboundconds.ProfileFile))
         tsinp.write("{}\n".format(self.turbsim_vt.metboundconds.RefHt))
         tsinp.write("{}\n".format(self.turbsim_vt.metboundconds.URef))
         tsinp.write("{}\n".format(self.turbsim_vt.metboundconds.ZJetMax))
         tsinp.write("{}\n".format(self.turbsim_vt.metboundconds.PLExp))
         tsinp.write("{}\n".format(self.turbsim_vt.metboundconds.Z0))

         # Non-IEC Meteorological Boundary Conditions
         tsinp.write("\n")
         tsinp.write("----\n")
         tsinp.write("{}\n".format(self.turbsim_vt.noniecboundconds.Latitude))
         tsinp.write("{}\n".format(self.turbsim_vt.noniecboundconds.RICH_NO))
         tsinp.write("{}\n".format(self.turbsim_vt.noniecboundconds.UStar))
         tsinp.write("{}\n".format(self.turbsim_vt.noniecboundconds.ZI))
         tsinp.write("{}\n".format(self.turbsim_vt.noniecboundconds.PC_UW))
         tsinp.write("{}\n".format(self.turbsim_vt.noniecboundconds.PC_UV))
         tsinp.write("{}\n".format(self.turbsim_vt.noniecboundconds.PC_VW))

         # Spatial Coherence Parameters
         tsinp.write("\n")
         tsinp.write("----\n")
         tsinp.write("{}\n".format(self.turbsim_vt.spatialcoherance.SCMod1))
         tsinp.write("{}\n".format(self.turbsim_vt.spatialcoherance.SCMod2))
         tsinp.write("{}\n".format(self.turbsim_vt.spatialcoherance.SCMod3))
         tsinp.write('"%f %f"\n'%(self.turbsim_vt.spatialcoherance.InCDec1[0], self.turbsim_vt.spatialcoherance.InCDec1[1]))
         tsinp.write('"%f %f"\n'%(self.turbsim_vt.spatialcoherance.InCDec2[0], self.turbsim_vt.spatialcoherance.InCDec2[1]))
         tsinp.write('"%f %f"\n'%(self.turbsim_vt.spatialcoherance.InCDec3[0], self.turbsim_vt.spatialcoherance.InCDec3[1]))
         tsinp.write("{}\n".format(self.turbsim_vt.spatialcoherance.CohExp))

         # Coherent Turbulence Scaling Parameters
         tsinp.write("\n")
         tsinp.write("----\n")
         tsinp.write("{}\n".format(self.turbsim_vt.coherentTurbulence.CTEventPath))
         tsinp.write("{}\n".format(self.turbsim_vt.coherentTurbulence.CTEventFile))
         tsinp.write("{}\n".format(self.turbsim_vt.coherentTurbulence.Randomize))
         tsinp.write("{}\n".format(self.turbsim_vt.coherentTurbulence.DistScl))
         tsinp.write("{}\n".format(self.turbsim_vt.coherentTurbulence.CTLy))
         tsinp.write("{}\n".format(self.turbsim_vt.coherentTurbulence.CTLz))
         tsinp.write("{}\n".format(self.turbsim_vt.coherentTurbulence.CTStartTime))




s = TurbsimBuilder()
s.turbsim_vt.metboundconds.UserFile = 'tsim_user_turbulence_default.inp'
s.turbsim_vt.metboundconds.ProfileFile = 'default.profile'
s.execute()
