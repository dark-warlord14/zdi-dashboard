# ZDI-11-317: Novell ZENWorks Software Packaging Antique ActiveX Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-317
- **ZDI-CAN:** ZDI-CAN-1234
- **Date:** 2011-11-07
- **CVE:** CVE-2011-2658
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-317/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENWorks. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists due to the inclusion and usage of an antique ActiveX control (mscomct2.ocx: Tue Mar 14 18:39:28 2000). Though mscomct2.ocx has been killbitted, it is accessed by ZENWorks via an intermediate control (ISList.ISAvi) which is scriptable. Multiple vulnerabilities in mscomct2.ocx can be exploited to execute arbitrary code on the host system in the context of the browser.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/viewContent.do?externalId=7009570&sliceId=1

## Disclosure Timeline

- 2011-05-17 - Vulnerability reported to vendor
- 2011-11-07 - Coordinated public release of advisory
