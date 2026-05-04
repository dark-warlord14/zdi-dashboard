# ZDI-09-024: Safenet SoftRemote IKE Service Remote Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-024
- **ZDI-CAN:** ZDI-CAN-399
- **Date:** 2009-06-01
- **CVE:** CVE-2009-1943
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Safenet
- **Affected Products:** SoftRemote
- **Credit:** Ruben Santamarta
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-024/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Safenet Softremote IKE VPN service. Authentication is not required to exploit this vulnerability. The specific flaw exists in the ireIke.exe service listening on UDP port 62514. The process does not adequately handle long requests resulting in a stack overflow. Exploitation can result in complete system compromise under the SYSTEM credentials.

## Additional Details

The issue has been fixed in our release version 10.8.6, customers are advised to upgrade to this version.

## Disclosure Timeline

- 2008-10-28 - Vulnerability reported to vendor
- 2009-06-01 - Coordinated public release of advisory
