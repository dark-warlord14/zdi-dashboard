# ZDI-20-879: D-Link DAP-1860 HNAP SOAPAction Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-879
- **ZDI-CAN:** ZDI-CAN-10084
- **Date:** 2020-07-20
- **CVE:** CVE-2020-15631
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-1860
- **Credit:** chung96vn - Security Researcher of VinCSS (Member of Vingroup)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-879/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DAP-1860 WiFi extenders. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the HNAP service, which listens on TCP port 80 by default. When parsing the SOAPAction header, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10185

## Disclosure Timeline

- 2020-03-03 - Vulnerability reported to vendor
- 2020-07-20 - Coordinated public release of advisory
