# ZDI-24-615: Logsign Unified SecOps Platform Missing Authentication Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-615
- **ZDI-CAN:** ZDI-CAN-24169
- **Date:** 2024-06-12
- **CVE:** CVE-2024-5721
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Logsign
- **Affected Products:** Unified SecOps Platform
- **Credit:** Mehmet INCE (@mdisec) from PRODAFT.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-615/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Logsign Unified SecOps Platform. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the cluster HTTP API, which listens on TCP port 1924 when enabled. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Logsign has issued an update to correct this vulnerability. More details can be found at: https://support.logsign.net/hc/en-us/articles/19316621924754-03-06-2024-Version-6-4-8-Release-Notes

## Disclosure Timeline

- 2024-05-31 - Vulnerability reported to vendor
- 2024-06-12 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
