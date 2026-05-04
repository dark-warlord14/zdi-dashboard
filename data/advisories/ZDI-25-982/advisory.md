# ZDI-25-982: oobabooga text-generation-webui trust_remote_code Reliance on Untrusted Inputs Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-982
- **ZDI-CAN:** ZDI-CAN-26681
- **Date:** 2025-10-30
- **CVE:** CVE-2025-12487
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** oobabooga
- **Affected Products:** text-generation-webui
- **Credit:** Nicholas Zubrisky (@NZubrisky) of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-982/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of oobabooga text-generation-webui. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the trust_remote_code parameter provided to the join endpoint. The issue results from the lack of proper validation of a user-supplied argument before using it to load a model. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

oobabooga has issued an update to correct this vulnerability. More details can be found at: https://github.com/oobabooga/text-generation-webui/commit/b5a6904c4ac4049823396090360b6f566f4e4603

## Disclosure Timeline

- 2025-03-13 - Vulnerability reported to vendor
- 2025-10-30 - Coordinated public release of advisory
- 2025-10-30 - Advisory Updated
