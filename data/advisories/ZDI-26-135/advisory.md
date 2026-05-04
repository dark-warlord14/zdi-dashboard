# ZDI-26-135: LangChain LangGraph BaseCache Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-135
- **ZDI-CAN:** ZDI-CAN-28385
- **Date:** 2026-03-03
- **CVE:** CVE-2026-27794
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** LangChain
- **Affected Products:** LangGraph
- **Credit:** Peter Girnus (@gothburz), Demeng Chen, and Brandon Niemczyk of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-135/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of LangChain LangGraph. Authentication is not required to exploit this vulnerability. The specific flaw exists within the BaseCache class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

LangChain has issued an update to correct this vulnerability. More details can be found at: https://github.com/langchain-ai/langgraph/security/advisories/GHSA-mhr3-j7m5-c7c9

## Disclosure Timeline

- 2025-12-09 - Vulnerability reported to vendor
- 2026-03-03 - Coordinated public release of advisory
- 2026-03-03 - Advisory Updated
