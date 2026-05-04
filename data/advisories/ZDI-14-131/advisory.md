# ZDI-14-131: (Pwn2Own) Adobe Reader PDF417 Barcode Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-131
- **ZDI-CAN:** ZDI-CAN-2210
- **Date:** 2014-05-19
- **CVE:** CVE-2014-0511
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** VUPEN
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-131/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PDF417 barcodes. The issue lies in the failure to properly sanitize a user-supplied value. An attacker can leverage this vulnerability to execute code within the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://helpx.adobe.com/security/products/reader/apsb14-15.html

## Disclosure Timeline

- 2014-03-13 - Vulnerability reported to vendor
- 2014-05-19 - Coordinated public release of advisory
