# ZDI-12-180: Novell ZENWorks AdminStudio ISGrid.dll ActiveX Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-180
- **ZDI-CAN:** ZDI-CAN-1434
- **Date:** 2012-08-29
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Novell
- **Affected Products:** ZENworks Admin Studio
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-180/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENworks Admin Studio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ISGrid.dll ActiveX control. The process performs insufficient bounds checking on user-supplied data passed in the DoFindReplace() method which results in heap corruption. This vulnerability can be leveraged to execute code under the context of the process.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://kb.flexerasoftware.com/selfservice/microsites/search.do?cmd=displayKC&docType=kc&externalId=Q201079&sliceId=1&docTypeID=DT_HOTFIX_1_1&dialogID=125341070&stateId=00 125337386

## Disclosure Timeline

- 2011-11-04 - Vulnerability reported to vendor
- 2012-08-29 - Coordinated public release of advisory
