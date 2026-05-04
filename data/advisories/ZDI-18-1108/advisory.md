# ZDI-18-1108: (0Day) Wecon PIStudio cximageu Image Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1108
- **ZDI-CAN:** ZDI-CAN-6245
- **Date:** 2018-10-02
- **CVE:** CVE-2018-14814
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Wecon
- **Affected Products:** PIStudio
- **Credit:** Mat Powell - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1108/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Wecon PIStudio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of images within DAT files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of an administrator.

## Additional Details

Wecon has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/ICSA-18-277-01 This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/18/18 - ZDI sent the report to ICS-CERT 05/22/18 - ICS-CERT acknowledged, confirmed the report was sent to the vendor and sent an ICS-VU # 09/17/18 - ZDI asked ICS-CERT to confirm the report remains unpatched and to advise the vendor of the intent to publish the report as 0-day on 10/02/18 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-05-18 - Vulnerability reported to vendor
- 2018-10-02 - Coordinated public release of advisory
- 2021-12-02 - Advisory Updated
