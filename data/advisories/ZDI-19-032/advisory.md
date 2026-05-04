# ZDI-19-032: Schneider Electric IIoT Monitor UpgradeMgmt upload Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-032
- **ZDI-CAN:** ZDI-CAN-7120
- **Date:** 2019-01-16
- **CVE:** CVE-2018-7836
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** IIot Monitor
- **Credit:** rgod of 9sg Security Team - rgod@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-032/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Schneider Electric IIoT Monitor. Authentication is required to exploit this vulnerability but authentication can be easily bypassed. The specific flaw exists within the processing of the upload method of the UpgradeMgmt servlet, which listens on port 8080 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-008-02

## Disclosure Timeline

- 2018-08-14 - Vulnerability reported to vendor
- 2019-01-16 - Coordinated public release of advisory
