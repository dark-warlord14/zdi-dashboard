# ZDI-16-217: Foxit Reader ConvertToPDF GIF Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-217
- **ZDI-CAN:** ZDI-CAN-3559
- **Date:** 2016-03-23
- **CVE:** CVE-2016-4065
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** AbdulAziz Hariri - HPE Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-217/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ConvertToPDF plugin. A specially crafted GIF image can force Foxit Reader to read memory past the end of an allocated object. An attacker can use this information in conjunction with other vulnerabilities to execute code in the context of the process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php Resolved with Foxit Reader 7.3.4

## Disclosure Timeline

- 2016-02-04 - Vulnerability reported to vendor
- 2016-03-23 - Coordinated public release of advisory
