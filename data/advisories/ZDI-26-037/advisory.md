# ZDI-26-037: (0Day) Langflow PythonFunction Code Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-037
- **ZDI-CAN:** ZDI-CAN-27497
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0771
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Langflow
- **Affected Products:** Langflow
- **Credit:** Peter Girnus (@gothburz), William Gamazo Sanchez, and Alfredo Oliveira of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-037/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Langflow. Attack vectors and exploitability will vary depending on the configuration of the product. The specific flaw exists within the handling of Python function components. Depending upon product configuration, an attacker may be able to introduce custom Python code into a workflow. An attacker can leverage this vulnerability to execute code in the context of the application.

## Additional Details

07/18/25 – ZDI submitted the report to the vendor’s GitHub account 09/11/25 – ZDI asked for updates 10/10/25 – ZDI asked for the fix 12/10/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-07-18 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
