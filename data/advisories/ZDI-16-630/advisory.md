# ZDI-16-630: Advantech SUSIAccess Server UpgradeMgmt upload Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-630
- **ZDI-CAN:** ZDI-CAN-3876
- **Date:** 2016-12-13
- **CVE:** CVE-2016-9351
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:M/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** SUSIAccess Server
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-630/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech SUSIAccess Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the processing of the UpgradeMgmt servlet upload function. The issue lies in the failure to properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-336-04

## Disclosure Timeline

- 2016-09-01 - Vulnerability reported to vendor
- 2016-12-13 - Coordinated public release of advisory
