# ZDI-14-133: (0Day) SolarWinds Network Configuration Manager PEstrarg1 Heap Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-133
- **ZDI-CAN:** ZDI-CAN-1906
- **Date:** 2014-05-19
- **CVE:** CVE-2014-3459
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** SolarWinds
- **Affected Products:** Network Configuration Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-133/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SolarWinds Network Configuration Manager. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the PEstrarg1 property. The issue lies in a failure to validate the size of the input buffer before copying it into a fixed-size buffer on the heap. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180-day deadline. Vendor Contact Timeline: 08/28/2013 - Case disclosed to vendor 02/24/2014 - Original 180-day deadline passed 02/25/2014 - ZDI sent request for status 02/25/2014 - Vendor reported "pending release vehicle" 04/08/2014 - ZDI sent a request for update 04/08/2014 - Vendor reported "fixed in NCM 7.3 - due to ship in May" 04/08/2014 - ZDI granted extension to May 04/23/2014 - ZDI sent a request for update 04/23/2014 - Vendor reported "RC for 7.3 was just released yesterday. GA should be shortly." 05/08/2014 - ZDI requested "any update on this GA?" 05/08/2014 - Vendor replied that they cannot commit publically to a date 05/19/2014 - ZDI publicly disclosed -- Mitigation: The killbit can be set on this control to disable scripting within Internet Explorer by modifying the data value of the Compatibilty Flags DWORD within the following location in the registry: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\ActiveX Compatibility\4097BE25-98A9-4779-AFF4-2F268B299D38 If the Compatibility Flags value is set to 0x00000400, the control can no longer be instantiated inside the browser. For more information, please see: http://support.microsoft.com/kb/240797

## Disclosure Timeline

- 2013-08-28 - Vulnerability reported to vendor
- 2014-05-19 - Coordinated public release of advisory
