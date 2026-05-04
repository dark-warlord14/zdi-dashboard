# ZDI-14-071: WellinTech KingScada AEserver.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-071
- **ZDI-CAN:** ZDI-CAN-1780
- **Date:** 2014-04-10
- **CVE:** CVE-2014-0787
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** WellinTech
- **Affected Products:** KingScada
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-071/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of WellinTech KingScada. Authentication is not required to exploit this vulnerability. The specific flaw exists within the protocol parsing code contained in kxNetDispose.dll. The parent service is called AEserver.exe and listens on port 12401. The process performs arithmetic on an user-supplied value used to determine the size of a copy operation allowing a potential integer wrap to cause a stack buffer overflow. An unauthenticated attacker can leverage this vulnerability to execute code under the context of the SYSTEM user.

## Additional Details

WellinTech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-14-098-02

## Disclosure Timeline

- 2014-02-25 - Vulnerability reported to vendor
- 2014-04-10 - Coordinated public release of advisory
