# ZDI-11-065: Adobe Reader Controlled memset Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-065
- **ZDI-CAN:** ZDI-CAN-842
- **Date:** 2011-02-08
- **CVE:** CVE-2011-0567
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Abdullah Ada
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-065/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within AcroRd32.dll. Initially, a pointer passed to memset can be miscalculated and the resulting copy operation corrupts heap memory. Later, the application attempts to use the modified data which can be leveraged to execute arbitrary code under the context of the user invoking the Reader application.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-03.html

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2011-02-08 - Coordinated public release of advisory
