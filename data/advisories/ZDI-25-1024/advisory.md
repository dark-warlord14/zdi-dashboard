# ZDI-25-1024: DreamFactory saveZipFile Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1024
- **ZDI-CAN:** ZDI-CAN-26589
- **Date:** 2025-11-26
- **CVE:** CVE-2025-13700
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** DreamFactory
- **Affected Products:** DreamFactory
- **Credit:** Catalin Iovita, David Bors, Alexandru Postolache
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1024/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of DreamFactory. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the saveZipFile method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

DreamFactory has issued an update to correct this vulnerability. More details can be found at: https://github.com/dreamfactorysoftware/df-core/commit/404a1783927f95999c71a0ff8f14130d385087fb

## Disclosure Timeline

- 2025-05-15 - Vulnerability reported to vendor
- 2025-11-26 - Coordinated public release of advisory
- 2025-11-26 - Advisory Updated
