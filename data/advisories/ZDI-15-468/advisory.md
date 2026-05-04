# ZDI-15-468: Adobe Reader Read Restrictions Bypass Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-468
- **ZDI-CAN:** ZDI-CAN-2893
- **Date:** 2015-10-13
- **CVE:** CVE-2015-5583
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** AbdulAziz Hariri and Jasiel Spelman of HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-468/
## Vulnerability Details

This vulnerability allows local attackers to disclose arbitrary PDF files on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Acrobat Reader printing. An attacker running code in the context of a sandboxed Adobe Reader process can print arbitrary PDF files on remote printers.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb15-24.html

## Disclosure Timeline

- 2015-04-21 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
