# ZDI-14-292: (0Day) (Pwn2Own) Microsoft Internet Explorer PresentationHost.exe Protected Mode Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-292
- **ZDI-CAN:** ZDI-CAN-2236
- **Date:** 2014-08-07
- **CVE:** CVE-2014-2819
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Zeguang Zhao of Team509 Liang Chen of KeenTeam
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-292/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of entries within the ElevationPolicy. The issue lies in the ability to call PresentationHost.exe to load a page outside of the sandbox. An attacker can leverage this vulnerability to execute code in the context of the current user at medium integrity.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 03/13/2014 - ZDI disclosed to vendor at Pwn2Own 03/14/2014 - Vendor acknowledged receipt 06/12/2014 - Vendor updated that they were "scoping/developing a fix" 07/09/2014 - Vendor requested an extension 07/14/2014 - ZDI granted extension to to 08/06/14 08/07/2014 - ZDI disclosed at Black Hat 08/12/2014 - Vendor patch posted -- Mitigation: Set the Policy value for PresentationHost.exe to either 0 or 2 within the ElevationPolicy in the registry. -- Vendor Response: Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS14-051

## Disclosure Timeline

- 2014-03-13 - Vulnerability reported to vendor
- 2014-08-07 - Coordinated public release of advisory
