# ZDI-13-207: Hewlett-Packard LoadRunner lrFileIOService ActiveX Control WriteFileString Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-207
- **ZDI-CAN:** ZDI-CAN-1705
- **Date:** 2013-08-13
- **CVE:** CVE-2013-4798
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** LoadRunner
- **Credit:** Brian Gorenc HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-207/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard LoadRunner. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the WriteFileString method. The method does not properly sanitize the destination path allowing for directory traversal. An attacker can leverage this vulnerability to write files and ultimately execute code under the context of the current user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03862772

## Disclosure Timeline

- 2013-01-07 - Vulnerability reported to vendor
- 2013-08-13 - Coordinated public release of advisory
