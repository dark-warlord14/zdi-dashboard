# ZDI-25-929: LiteLLM Information health API_KEY Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-929
- **ZDI-CAN:** ZDI-CAN-26585
- **Date:** 2025-10-03
- **CVE:** CVE-2025-11203
- **CVSS:** 3.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** LiteLLM
- **Affected Products:** LiteLLM
- **Credit:** David Fiser and Alfredo Oliveira of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-929/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of LiteLLM. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of the API_KEY parameter provided to the health endpoint. The issue results from exposing sensitive information to an unauthorized actor. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

LiteLLM has issued an update to correct this vulnerability. More details can be found at: https://docs.litellm.ai/release_notes/v1.63.14-stable

## Disclosure Timeline

- 2025-03-25 - Vulnerability reported to vendor
- 2025-10-03 - Coordinated public release of advisory
- 2025-10-03 - Advisory Updated
