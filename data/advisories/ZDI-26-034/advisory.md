# ZDI-26-034: (0Day) Langflow code Code Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-034
- **ZDI-CAN:** ZDI-CAN-27322
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0768
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Langflow
- **Affected Products:** Langflow
- **Credit:** Peter Girnus (@gothburz), William Gamazo Sanchez, and Alfredo Oliveira of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-034/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Langflow. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the code parameter provided to the validate endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute Python code. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

07/18/25 – ZDI submitted the report to the vendor’s GitHub account 09/11/25 – ZDI asked for updates 10/10/25 – ZDI asked for the fix 12/10/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-07-18 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
