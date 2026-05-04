# ZDI-25-1143: (0Day) Hugging Face smolagents Remote Python Executor Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1143
- **ZDI-CAN:** ZDI-CAN-28312
- **Date:** 2025-12-18
- **CVE:** CVE-2025-14931
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Hugging Face
- **Affected Products:** smolagents
- **Credit:** Peter Girnus (@gothburz), Demeng Chen, and Brandon Niemczyk of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1143/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hugging Face smolagents. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of pickle data. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

12/09/25 - ZDI submitted the report to a third-party bug bounty program 12/10/25 - the report was rejected for being out of scope for the bug bounty program 12/11/24 – the vendor closed the case as a duplicate of another report 12/12/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/18/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-12-09 - Vulnerability reported to vendor
- 2025-12-18 - Coordinated public release of advisory
- 2025-12-18 - Advisory Updated
