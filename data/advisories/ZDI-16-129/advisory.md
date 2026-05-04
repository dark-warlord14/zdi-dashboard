# ZDI-16-129: Advantech WebAccess Dashboard Viewer saveGeneralFile Arbitrary File Creation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-129
- **ZDI-CAN:** ZDI-CAN-3128
- **Date:** 2016-02-05
- **CVE:** CVE-2016-0854
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-129/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the WebAccess Dashboard Viewer. Insufficient validation within the SaveGeneralFile functionality allows unauthenticated callers to upload arbitrary code to directories in the server where the code can be automatically executed under the high-privilege context of the IIS AppPool. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-014-01

## Disclosure Timeline

- 2015-09-15 - Vulnerability reported to vendor
- 2016-02-05 - Coordinated public release of advisory
