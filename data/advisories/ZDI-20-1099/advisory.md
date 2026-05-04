# ZDI-20-1099: (0Day) Hewlett Packard Enterprise Pay per use UCS Meter ReceiverServlet doGet Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1099
- **ZDI-CAN:** ZDI-CAN-10603
- **Date:** 2020-09-08
- **CVE:** CVE-2020-24625
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Pay per use UCS Meter
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1099/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Hewlett Packard Enterprise Pay per use UCS Meter. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ReceiverServlet class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose files in the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 04/14/20 - ZDI reported the vulnerability to the vendor 05/05/20 - The vendor confirmed receipt of the report 08/18/20 - ZDI requested an update 08/20/20 - The vendor replied that a fix would be available in September 08/20/20 - ZDI offered an extension until 09/05/2020 08/20/20 - The vendor confirmed that a fix will not be available by 09/05/20 08/31/20 - ZDI notified the vendor of the intention to publish these reports as 0-day advisories on 09/07/2020 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application. https://support.hpe.com/hpesc/public/docDisplay?docLocale=en_US&docId=hpesbgn04037en_us

## Disclosure Timeline

- 2020-04-14 - Vulnerability reported to vendor
- 2020-09-08 - Coordinated public release of advisory
- 2020-10-01 - Advisory Updated
