# ZDI-21-151: (0Day) Hewlett Packard Enterprise Moonshot Provisioning Manager khuploadfile Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-151
- **ZDI-CAN:** ZDI-CAN-11830
- **Date:** 2021-02-04
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Moonshot Provisioning Manager
- **Credit:** Sivathmican Sivakumaran
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-151/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hewlett Packard Enterprise Moonshot Provisioning Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the khuploadfile.cgi binary. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 09/04/20 – ZDI reported the vulnerabilities to the vendor 09/04/20 – The vendor acknowledged the report 01/20/21 – ZDI requested an update 01/21/21 – The vendor indicated the product was End Of Life and not supported 01/21/21 – ZDI requested details of the public notification 01/22/21 – The vendor indicated they could not provide any customer facing notification as they were still documenting the product as End Of Life 01/29/21 – ZDI notified the vendor of the intention to publish the reports as 0-day advisories on 02/04/21 02/02/21 – The vendor released a note indicating the End Of Life status of the product -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-09-04 - Vulnerability reported to vendor
- 2021-02-04 - Coordinated public release of advisory
