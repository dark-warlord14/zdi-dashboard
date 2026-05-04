# ZDI-13-048: Novell ZENWorks AdminStudio ISProxy ActiveX Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-048
- **ZDI-CAN:** ZDI-CAN-1433
- **Date:** 2013-03-22
- **CVE:** CVE-2013-1079
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Novell
- **Affected Products:** ZENworks Admin Studio
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-048/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENworks Admin Studio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ISProxy.dll ActiveX object. The ISCreateObject() method suffers from a directory vulnerability and it is also possible to break the search path through a null char. By combining the Initialize() and ISCreateObject() methods, an attacker can force the underlying operating system to load arbitrary dlls bypassing normal security restriction. This vulnerability allows an attacker to execute code under the context of the process.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/kb/doc.php?id=7011811

## Disclosure Timeline

- 2011-11-29 - Vulnerability reported to vendor
- 2013-03-22 - Coordinated public release of advisory
