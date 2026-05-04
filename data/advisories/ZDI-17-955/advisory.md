# ZDI-17-955: NetGain Systems Enterprise Manager MainFilter doFilter Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-955
- **ZDI-CAN:** ZDI-CAN-5099
- **Date:** 2017-12-13
- **CVE:** CVE-2017-16590
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** NetGain Systems
- **Affected Products:** Enterprise Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-955/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of NetGain Systems Enterprise MainFilter. User interaction is required to exploit this vulnerability. The specific flaw exists within the MainFilter servlet. The issue results from the lack of proper string matching inside the doFilter method. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of Administrator.

## Additional Details

Fixed for NetGain Enterprise Manager - fixed version: v7.2.766 and above

## Disclosure Timeline

- 2017-09-06 - Vulnerability reported to vendor
- 2017-12-13 - Coordinated public release of advisory
