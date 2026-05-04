# ZDI-21-150: (0Day) Hewlett Packard Enterprise Moonshot Provisioning Manager khuploadfile Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-150
- **ZDI-CAN:** ZDI-CAN-11707
- **Date:** 2021-02-04
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Moonshot Provisioning Manager
- **Credit:** Erik de Jong
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-150/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of Hewlett Packard Enterprise Moonshot Provisioning Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the khuploadfile.cgi binary. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 09/04/20 – ZDI reported the vulnerabilities to the vendor 09/04/20 – The vendor acknowledged the report 01/20/21 – ZDI requested an update 01/21/21 – The vendor indicated the product was End Of Life and not supported 01/21/21 – ZDI requested details of the public notification 01/22/21 – The vendor indicated they could not provide any customer facing notification as they were still documenting the product as End Of Life 01/29/21 – ZDI notified the vendor of the intention to publish the reports as 0-day advisories on 02/04/21 02/02/21 – The vendor released a note indicating the End Of Life status of the product -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-09-04 - Vulnerability reported to vendor
- 2021-02-04 - Coordinated public release of advisory
