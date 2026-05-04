# ZDI-26-307: FlowiseAI Flowise Airtable_Agent Code Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-307
- **ZDI-CAN:** ZDI-CAN-29412
- **Date:** 2026-05-01
- **CVE:** CVE-2026-41265
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Flowise
- **Affected Products:** Flowise
- **Credit:** Dre Cura (@dre_cura) and Nicholas Zubrisky (@NZubrisky) of TrendAI Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-307/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Flowise. Authentication is not required to exploit this vulnerability. The specific flaw exists within the run method of the Airtable_Agents class. The issue results from the lack of proper validation of a user-supplied string before using it to execute Python code. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Flowise has issued an update to correct this vulnerability. More details can be found at: https://github.com/FlowiseAI/Flowise/commit/cf36fb71fbd33437166f8a94de8534a4d9b6180c

## Disclosure Timeline

- 2026-02-26 - Vulnerability reported to vendor
- 2026-05-01 - Coordinated public release of advisory
- 2026-05-01 - Advisory Updated
