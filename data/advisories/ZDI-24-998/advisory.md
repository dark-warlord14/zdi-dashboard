# ZDI-24-998: KernelCI SAS Token Incorrect Permission Assignment Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-998
- **ZDI-CAN:** ZDI-CAN-22317
- **Date:** 2024-07-29
- **CVE:** N/A
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:L
- **Affected Vendors:** KernelCI
- **Affected Products:** KernelCI
- **Credit:** Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-998/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on KernelCI. Authentication is not required to exploit this vulnerability. The specific flaw exists within the permissions granted to an SAS token. An attacker can leverage this vulnerability to make unauthorized changes to KernelCI build data.

## Additional Details

KernelCI has issued an update to correct this vulnerability. More details can be found at: https://github.com/kernelci/kernelci-project/commit/94be815f992f73e6ddc5dfdd4c6d458dc86cfce0

## Disclosure Timeline

- 2023-10-12 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
