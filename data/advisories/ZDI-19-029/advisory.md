# ZDI-19-029: Schneider Electric IIoT Monitor DeviceMapMgmt upload Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-029
- **ZDI-CAN:** ZDI-CAN-7135
- **Date:** 2019-01-14
- **CVE:** CVE-2018-7836
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IIot Monitor
- **Credit:** rgod of 9sg Security Team - rgod@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-029/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Schneider Electric IIoT Monitor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of the upload method of the DeviceMapMgmt servlet. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-008-02

## Disclosure Timeline

- 2018-08-14 - Vulnerability reported to vendor
- 2019-01-14 - Coordinated public release of advisory
