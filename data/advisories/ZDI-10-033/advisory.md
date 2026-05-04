# ZDI-10-033: Microsoft Internet Explorer TIME2 Behavior Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-033
- **ZDI-CAN:** ZDI-CAN-548
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0492
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Simon Zuckerbraun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-033/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious web page. The issue is located within the CTimeAction object. During handling of the TIME2 behavior, an attacker can trick the application into destroying the markup causing the application to reference memory that has previously been freed. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms10-018.mspx

## Disclosure Timeline

- 2009-08-10 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory
