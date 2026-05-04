# ZDI-13-056: Cisco IOS Smart Install Configuration File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-056
- **ZDI-CAN:** ZDI-CAN-1568
- **Date:** 2013-04-09
- **CVE:** CVE-2013-1146
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** IOS
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-056/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco IOS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Smart Install client. A specially crafted packet can be sent to the SMI IBC server to instruct it to download the IOS config file and IOS image file(s). The vulnerability allows the attacker to replace the startup configuration file and the booting IOS image on Cisco switches running as a Smart Install client. The attacker can specify a user account with highest access in the config file, allowing them to take complete control of the switch.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20130327-smartinstall

## Disclosure Timeline

- 2012-07-24 - Vulnerability reported to vendor
- 2013-04-09 - Coordinated public release of advisory
