# ZDI-23-633: D-Link DIR-2150 GetFirmwareStatus Target Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-633
- **ZDI-CAN:** ZDI-CAN-20561
- **Date:** 2023-05-15
- **CVE:** CVE-2023-34281
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-2150
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-633/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DIR-2150 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the SOAP API interface, which listens on TCP port 80 by default. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in Firmware v1.06 https://support.dlink.com.au/Download/download.aspx?product=DIR-2150

## Disclosure Timeline

- 2023-04-28 - Vulnerability reported to vendor
- 2023-05-15 - Coordinated public release of advisory
- 2023-06-02 - Advisory Updated
