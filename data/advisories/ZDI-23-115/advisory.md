# ZDI-23-115: VMware vRealize Log Insight RemotePakDownloadCommand Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-115
- **ZDI-CAN:** ZDI-CAN-17962
- **Date:** 2023-02-09
- **CVE:** CVE-2022-31706
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** vRealize
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-115/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of VMware vRealize Log Insight. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RemotePakDownloadCommand function. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2023-0001.html

## Disclosure Timeline

- 2022-08-31 - Vulnerability reported to vendor
- 2023-02-09 - Coordinated public release of advisory
