# ZDI-16-058: Advantech WebAccess webvrpcs Service BwpAlarm.dll ProjectName strcpy Globals Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-058
- **ZDI-CAN:** ZDI-CAN-3243
- **Date:** 2016-02-05
- **CVE:** CVE-2016-0860
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-058/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable instances of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the 0x11173 IOCTL in the BwpAlarm subsystem. A globals overflow vulnerability exists in a call to strcpy using the ProjectName parameter. An attacker can use this vulnerability to execute arbitrary code in the context of an administrator of the system.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-014-01

## Disclosure Timeline

- 2015-09-17 - Vulnerability reported to vendor
- 2016-02-05 - Coordinated public release of advisory
