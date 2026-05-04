# ZDI-25-312: Hewlett Packard Enterprise StoreOnce VSA setLocateBeaconOnHardware Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-312
- **ZDI-CAN:** ZDI-CAN-24981
- **Date:** 2025-06-02
- **CVE:** CVE-2025-37089
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** StoreOnce VSA
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-312/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hewlett Packard Enterprise StoreOnce VSA. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the implementation of the setLocateBeaconOnHardware method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbst04847en_us&docLocale=en_US

## Disclosure Timeline

- 2024-10-31 - Vulnerability reported to vendor
- 2025-06-02 - Coordinated public release of advisory
- 2025-06-02 - Advisory Updated
