# ZDI-24-1077: (0Day) (Pwn2Own) oFono QMI SMS Handling Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1077
- **ZDI-CAN:** ZDI-CAN-23157
- **Date:** 2024-08-05
- **CVE:** CVE-2024-7537
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** oFono
- **Affected Products:** oFono
- **Credit:** Rob Blakely
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1077/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of oFono. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of SMS message lists. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

08/05/24 – ZDI made multiple attempts to report the vulnerability to the vendor via the oFono distribution list, Red Hat, and upstream Linux Kernel, but the vendor did not respond. The Linux Kernel informed ZDI that since it “has nothing to do with the Linux Kernel,” we should report it to the distribution list. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-02-01 - Vulnerability reported to vendor
- 2024-08-05 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
