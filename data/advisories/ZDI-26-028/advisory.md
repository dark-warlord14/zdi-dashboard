# ZDI-26-028: (0Day) GPT Academic stream_daas Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-028
- **ZDI-CAN:** ZDI-CAN-27956
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0762
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** GPT Academic
- **Affected Products:** GPT Academic
- **Credit:** Peter Girnus (@gothburz) and Brandon Niemczyk of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-028/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GPT Academic. Interaction with a malicious DAAS server is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the stream_daas function. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

08/27/25 – ZDI submitted the report to the vendor 09/24/25 – ZDI asked for updates 10/22/25 – ZDI asked for updates 12/10/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-08-27 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
