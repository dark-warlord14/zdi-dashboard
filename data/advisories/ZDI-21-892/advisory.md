# ZDI-21-892: (0Day) Apple macOS ImageIO WEBP File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-892
- **ZDI-CAN:** ZDI-CAN-12842
- **Date:** 2021-07-22
- **CVE:** CVE-2021-30706
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-892/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the ImageIO library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the ImageIO framework. Crafted data in a WEBP file can trigger a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/26/21 – ZDI reported the vulnerability to the vendor 05/26/21 – ZDI requested an update 06/04/21 – ZDI requested an update 06/16/21 – ZDI requested an update 06/18/21 – ZDI requested an update and notified the vendor of the intention to publish the report as a 0-day advisory 06/18/21 – The vendor indicated the case would be published in an upcoming advisory 06/22/21 – ZDI requested a more specific date for the advisory 07/07/21 – ZDI requested an update 07/07/21 – The vendor indicated the issue had been addressed and would be published in an upcoming update 07/08/21 – ZDI requested a more specific date for the advisory 07/09/21 – The vendor indicated the advisory would be available by the end of the following week 07/12/21 – ZDI agreed to hold advisories for a few days 07/20/21 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 07/22/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-02-25 - Vulnerability reported to vendor
- 2021-07-22 - Coordinated public release of advisory
