# ZDI-11-319: Novell ZENWorks Software Packaging ISGrid.Grid2.1 DoFindReplace bstrReplaceText Parameter Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-319
- **ZDI-CAN:** ZDI-CAN-1235
- **Date:** 2011-11-07
- **CVE:** CVE-2011-3174
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-319/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENWorks. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within \Program Files\Common Files\InstallShield\ISGrid2.dll. If the bstrReplaceText parameter exceeds its statically-allocated length then a buffer overflow will occur. This can be exploited to execute arbitrary code on the system in the context of the user running the browser.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/viewContent.do?externalId=7009570&sliceId=1

## Disclosure Timeline

- 2011-05-17 - Vulnerability reported to vendor
- 2011-11-07 - Coordinated public release of advisory
