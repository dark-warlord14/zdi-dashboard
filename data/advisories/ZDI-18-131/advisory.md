# ZDI-18-131: Novell NetIQ Access Manager OspUIBasicSSODownload Servlet fileInfo1 Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-131
- **ZDI-CAN:** ZDI-CAN-5087
- **Date:** 2018-01-19
- **CVE:** CVE-2017-14803
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Novell
- **Affected Products:** NetIQ Access Manager
- **Credit:** rgod and kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-131/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Novell NetIQ Access Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the downloadBasicSSOServlet servlet. When parsing the fileInfo1 parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: https://www.novell.com/support/kb/doc.php?id=7022443

## Disclosure Timeline

- 2017-08-21 - Vulnerability reported to vendor
- 2018-01-19 - Coordinated public release of advisory
