# ZDI-14-224: (0Day) Embarcadero ER/Studio Data Architect TSVisualization ActiveX loadExtensionFactory Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-224
- **ZDI-CAN:** ZDI-CAN-2302
- **Date:** 2014-07-09
- **CVE:** CVE-2014-4647
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Embarcadero
- **Affected Products:** ER/Studio Data Architect
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-224/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Embarcadero ER/Studio Data Architect. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the loadExtensionFactory method. The issue lies in the failure to validate the size of the input buffer before copying it into a fixed-size buffer on the stack. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI vulnerability disclosure policy on lack of vendor response. Vendor Contact Timeline: 05/12/2014 - Submitted Contact Us form/request for contact at vendor site 05/12/2014 - Automated reply from vendor 05/14/2014 - Reply from vendor 05/15/2014 - ZDI requested a PGP key for disclosure (no reply) 05/19/2014 - ZDI requested a PGP key for disclosure (no reply) 06/09/2014 - ZDI requested a PGP key for disclosure (no reply) -- Mitigation: The killbit can be set on this control to disable scripting within Internet Explorer by modifying the data value of the Compatibilty Flags DWORD within the following location in the registry: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\ActiveX Compatibility\B4D34128-82FF-4B87-94A0-F5D4CC1FE3D0 If the Compatibility Flags value is set to 0x00000400, the control can no longer be instantiated inside the browser. For more information, please see: http://support.microsoft.com/kb/240797

## Disclosure Timeline

- 2014-05-12 - Vulnerability reported to vendor
- 2014-07-09 - Coordinated public release of advisory
