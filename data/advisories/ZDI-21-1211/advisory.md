# ZDI-21-1211: (0Day) Fuji Electric Alpha5 A5V File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1211
- **ZDI-CAN:** ZDI-CAN-13999
- **Date:** 2021-10-15
- **CVE:** CVE-2022-21202
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Alpha5
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1211/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Fuji Electric Alpha5. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of A5V files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 06/11/21 – ZDI reported the vulnerability to the vendor 09/02/21 – ICS-CERT indicated the vendor has been notified and requested an extension 09/03/21 – ZDI agreed to give them an extension 10/04/21 – ZDI requested an update 10/04/21 – ICS-CERT indicated that the vendor would have the fix ready by 12/31/21 10/05/21 – ZDI notified ICS-CERT of the intention to publish the case as a 0-day advisory on 10/14/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-06-11 - Vulnerability reported to vendor
- 2021-10-15 - Coordinated public release of advisory
- 2022-03-23 - Advisory Updated
