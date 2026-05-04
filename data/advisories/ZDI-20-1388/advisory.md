# ZDI-20-1388: McAfee Total Protection Junction Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1388
- **ZDI-CAN:** ZDI-CAN-11575
- **Date:** 2020-12-01
- **CVE:** CVE-2020-7335
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** McAfee
- **Affected Products:** Total Protection
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1388/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of McAfee Total Protection. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of junctions. By creating a junction, an attacker can abuse the product to overwrite the contents of a chosen file. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

McAfee has issued an update to correct this vulnerability. More details can be found at: https://service.mcafee.com/webcenter/portal/oracle/webcenter/page/scopedMD/s55728c97_466d_4ddb_952d_05484ea932c6/Page29.jspx?wc.contextURL=%2Fspaces%2Fcp&articleId=TS103089&_afrLoop=70260263328735&leftWidth=0%25&showFooter=false&showHeader=false&rightWidth=0%25¢erWidth=100%25#!%40%40%3FshowFooter%3Dfalse%26_afrLoop%3D70260263328735%26articleId%3DTS103089%26leftWidth%3D0%2525%26showHeader%3Dfalse%26wc.contextURL%3D%252Fspaces%252Fcp%26rightWidth%3D0%2525%26centerWidth%3D100%2525%26_adf.ctrl-state%3D8p9y2e9ky_31

## Disclosure Timeline

- 2020-08-19 - Vulnerability reported to vendor
- 2020-12-01 - Coordinated public release of advisory
