# ZDI-21-127: (0Day) Apache Dubbo readUTF Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-127
- **ZDI-CAN:** ZDI-CAN-11482
- **Date:** 2021-02-02
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apache
- **Affected Products:** Dubbo
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-127/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apache Dubbo. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the Dubbo protocol. Crafted data in a Dubbo protocol message can trigger the deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 08/26/20 – ZDI reported the vulnerability to the vendor 08/26/20 – The vendor acknowledged the report 01/05/21 – ZDI requested an update 01/18/21 – The vendor indicated they were waiting for a response from the responsible team 01/18/21 – ZDI notified the vendor of the intention to publish the reports as 0-day advisories 01/28/21 – ZDI notified the vendor of the intention to publish the reports as 0-day advisories on 02/02/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-08-26 - Vulnerability reported to vendor
- 2021-02-02 - Coordinated public release of advisory
