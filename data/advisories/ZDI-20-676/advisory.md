# ZDI-20-676: Trend Micro InterScan Web Security Virtual Appliance Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-676
- **ZDI-CAN:** ZDI-CAN-10095
- **Date:** 2020-05-27
- **CVE:** CVE-2020-8605
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** InterScan Web Security Virtual Appliance
- **Credit:** Mehmet INCE (@mdisec)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-676/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trend Micro InterScan Web Security Virtual Appliance. Authentication is required to exploit this vulnerability. The specific flaw exists within the LogSettingHandler class. When parsing the mount_device parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

https://success.trendmicro.com/solution/000253095

## Disclosure Timeline

- 2020-01-17 - Vulnerability reported to vendor
- 2020-05-27 - Coordinated public release of advisory
- 2020-05-28 - Advisory Updated
